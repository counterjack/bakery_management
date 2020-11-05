from rest_framework.permissions import BasePermission
from user.models import UserProxy

class IsCustomer(BasePermission):
    """
    Allows access only to customers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and UserProxy.is_customer(request.user))


class IsVendor(BasePermission):
    """
    Allows access only to Vendors.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and UserProxy.is_vendor(request.user))