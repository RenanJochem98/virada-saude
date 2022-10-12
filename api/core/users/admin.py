from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from anamnese.models import Anamnese

#from users.models import RegistrationForm

User = get_user_model()


# @admin.register(RegistrationForm)
# class RegistrationFormAdmin(admin.ModelAdmin):
#     model = RegistrationForm
#     list_display = ["name"]

#     def changelist_view(self, request, *args, **kwargs):
#         self.request = request
#         return super().changelist_view(request, *args, **kwargs)

# class AnamneseInline(admin.TabularInline):
#     model = Anamnese
#     extra = 0

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id", "email", "first_name", "last_name", "empresa", "anamnese", "is_active", "is_staff", "is_superuser"
    )

    # list_filter = ("is_active", "empresa", "is_active", "is_staff", "is_superuser")
    search_fields = ("email", "first_name", "last_name", "empresa")

    list_editable=('first_name', 'last_name', "empresa", "is_active", "is_staff", "is_superuser")
    ordering = ("id",)
    # exclude = ('dat_emission', )
    # inlines = [AnamneseInline]
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
                "fields": ("email", "password1", "password2",
                            "first_name", "last_name", "empresa", "is_active", "is_staff", "is_superuser"),
            },
        ),
    )
    


admin.site.unregister(Group)
