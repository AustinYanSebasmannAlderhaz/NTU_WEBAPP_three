from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthenticatedReadOnlyStaffWrite(BasePermission):
    """
    Read access: authenticated users
    Write access: staff users only
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True

        return user.is_staff
