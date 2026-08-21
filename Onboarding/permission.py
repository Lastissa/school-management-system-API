"""
CONTROL PERMISSION OF WHO IS ALLOWED TO DO THIS OR THAT IN ONBOARDING
"""
from rest_framework.permissions import BasePermission



class OnboardMngt(BasePermission):
    """Permission restricted to only admin and management"""
    def has_permission(self, request, view):
        allow_mngts = request.user.is_authenticated and request.user.is_mngt
        allow_admin = request.user.is_authenticated and request.user.is_superuser
        return allow_admin or allow_mngts
