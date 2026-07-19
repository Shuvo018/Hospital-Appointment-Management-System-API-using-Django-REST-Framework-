from hospital_management.models import Doctor, User
from rest_framework import serializers

class DoctorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'name', 'department', 'specialization', 'visiting_fee', 'created_at', 'updated_at']
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_user(self, user):
        # Ensure selected user is a doctor
        if user.role != User.Role.DOCTOR:
            raise serializers.ValidationError(
                "Selected user must have DOCTOR role."
            )

        # Prevent duplicate doctor profile
        if Doctor.objects.filter(user=user).exists():
            raise serializers.ValidationError(
                "This user already has a doctor profile."
            )
        return user
    
class DoctorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", read_only=True)
    phone_number = serializers.CharField(source="user.phone_number", read_only=True)

    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "department",
            "specialization",
            "visiting_fee",
            "email",
            "phone_number",
        ]
