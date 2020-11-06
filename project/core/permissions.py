from rest_framework.permissions import BasePermission
from user.models import UserProxy
from bakery.models import Bakery
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
        if not request.user or not request.user.is_authenticated or UserProxy.is_vendor(request.user):
            return False
        # Otherwise Set the bakery object to request object itself
        request.user.bakery = Bakery.objects.filter(owner=request.user).first()
        return True