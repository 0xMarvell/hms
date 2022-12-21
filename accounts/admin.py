from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering = ('-start_date',)
    list_display = ('first_name', 'last_name', 'email','is_staff', 'is_patient', 'is_health_worker')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_patient', 'is_health_worker')}),
        # ('Personal', {'fields': ('about',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name',
                'phone_number','is_patient', 'is_health_worker',
                'password1', 'password2', 'is_active', 'is_staff',
                )}
         ),
    )

admin.site.register(User, UserAdminConfig)
