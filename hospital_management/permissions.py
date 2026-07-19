from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsDoctorOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "Doctor"
        )

class IsPatientOnly(BasePermission):
    def has_permission(self, request, view):
            return (
                request.user.is_authenticated
                and request.user.role == "Patient"
            )
