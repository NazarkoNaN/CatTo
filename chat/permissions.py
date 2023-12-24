from rest_framework import permissions
from rest_framework import authtoken


class IsSenderOrRceiverToReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permission are allowed for any members
        if request.method in permissions.SAFE_METHODS and request.user in obj.chat.receivers:
            return True
        
        # Write permission are allowed for author only
        return obj.sender == request.user


class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.user in obj.receivers:
            return True