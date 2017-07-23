from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UserAdmin(UserAdmin):
    form = UserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('profile_image',)}),
    )


admin.site.register(User, UserAdmin)