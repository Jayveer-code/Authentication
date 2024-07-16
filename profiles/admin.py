from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob',)
    search_fields = ('user__username', 'user__email', 'dob',)
    list_filter = ('dob',)
    fieldsets = (
        (None, {
            'fields': ('user', 'dob',)
        }),
    )
    readonly_fields = ('user',)

    def has_delete_permission(self, request, obj=None):
        return False
