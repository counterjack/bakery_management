from django.db import models
from core.models import DateCreatedUpdatedTimeMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class UserType(models.TextChoices):
    CUSTOMER = _("CUSTOMER")
    VENDOR = _("VENDOR")

class UserProfile(DateCreatedUpdatedTimeMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        choices=UserType.choices,
        default=UserType.CUSTOMER,
        null=False,
        max_length=20
    )
    phone = models.CharField(max_length=10, null=False, blank=False)
    is_verified = models.BooleanField(default=False)


class UserProxy(User):
    class Meta:
        proxy = True

    def is_customer(self) -> bool:
        return self.userprofile.user_type == UserType.CUSTOMER

    def is_vendor(self) -> bool:
        return self.userprofile.user_type == UserType.VENDOR