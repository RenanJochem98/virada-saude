from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from users.models import RegistrationForm

User = get_user_model()


# @admin.register(RegistrationForm)
# class RegistrationFormAdmin(admin.ModelAdmin):
#     model = RegistrationForm
#     list_display = ["name"]

#     def changelist_view(self, request, *args, **kwargs):
#         self.request = request
#         return super().changelist_view(request, *args, **kwargs)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "is_active",
    )
    ordering = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_filter = ("is_active",)
    search_fields = ("email", "username")


admin.site.unregister(Group)
