from django.contrib import admin

# # Register your models here.
from .models import User

admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email','get_full_name','is_active','phone','nrc','dob','is_verified' )
#     search_fields = ('first_name','last_name','phone' )
#     list_filter = ('is_staff','is_active','country','is_verified')

#     actions = ['verify','unverify','activate' ,'deactivate' ]

#     def verify(self, queryset):
#         queryset.update(is_verified=True)

#     def unverify(self, queryset):
#         queryset.update(is_verified=False)

#     def activate(self, queryset):
#         queryset.update(is_active=True)

#     def deactivate(self, queryset):
#         queryset.update(is_active=False)
