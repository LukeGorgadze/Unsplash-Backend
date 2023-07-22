from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests for authenticated users who are the owners of the photo item
        return request.method == 'GET' and request.user == obj.user