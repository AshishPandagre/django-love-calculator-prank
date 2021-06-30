from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Referral, Contact


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'key',
                ),
            },
        ),
    )

    list_display = ['username', 'first_name', 'last_name', 'key']


admin.site.register(User, CustomUserAdmin)

class ReferralAdmin(admin.ModelAdmin):
    list_display = ['_from', 'name', 'crush']

admin.site.register(Referral, ReferralAdmin)
admin.site.register(Contact)
