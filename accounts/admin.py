from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import * 


 
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("email", "user_type", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active", 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ('user_type', "is_staff", "is_active", "groups", "user_permissions", 'is_crm', 'is_verified')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'id_type', 'id_number','dob', 'country', 'phone', 'location', 'profile_pic')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)  # Replace YourModelName with the actual name of your model

 
