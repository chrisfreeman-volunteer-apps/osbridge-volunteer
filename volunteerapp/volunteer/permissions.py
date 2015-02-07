from rest_framework import permissions


class IsObjectAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    If the user is authenticated, (s)he can create new objects.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # For all other submissions
        # Write permissions are only allowed if user is admin of the object.
        return (request.user.is_authenticated()
                and obj.admin.filter(id=request.user.id).exists())
