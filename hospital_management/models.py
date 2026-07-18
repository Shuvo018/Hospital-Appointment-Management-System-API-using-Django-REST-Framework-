from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.PATIENT)

    # Profile fields (Full Name is covered by first_name/last_name from AbstractUser)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"

    @property
    def full_name(self):
        return self.get_full_name()


class Doctor(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
        limit_choices_to={"role": User.Role.DOCTOR},
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=150)
    visiting_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0, message="Visiting fee cannot be negative.")],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def clean(self):
        if self.visiting_fee is not None and self.visiting_fee < 0:
            raise ValidationError({"visiting_fee": "Visiting fee cannot be negative."})

    def __str__(self):
        return f"Dr. {self.name} ({self.department})"


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments",
        limit_choices_to={"role": User.Role.PATIENT},
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-appointment_date", "-appointment_time"]

    def clean(self):
        if self.appointment_date and self.appointment_date < timezone.localdate():
            raise ValidationError(
                {"appointment_date": "Appointment date cannot be in the past."}
            )

    def __str__(self):
        return f"{self.patient} -> {self.doctor} on {self.appointment_date} {self.appointment_time} [{self.status}]"


class Bill(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bills",
        limit_choices_to={"role": User.Role.PATIENT},
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="bills",
    )
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="bill",
    )
    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.discount is not None and self.consultation_fee is not None:
            if self.discount > self.consultation_fee:
                raise ValidationError(
                    {"discount": "Discount cannot be greater than consultation fee."}
                )

    def save(self, *args, **kwargs):
        # Auto-calculate total_amount = consultation_fee - discount
        self.full_clean(exclude=[f.name for f in self._meta.fields if f.name not in
                                  ("discount", "consultation_fee")])
        self.total_amount = (self.consultation_fee or 0) - (self.discount or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.pk} - {self.patient} - {self.total_amount}"