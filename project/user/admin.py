from django.contrib import admin
from user.models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass