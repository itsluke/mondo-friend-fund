from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mondo_user_id', 'mondo_account_id', 'user')
    search_fields = ['user__email']


admin.site.register(Profile, ProfileAdmin)
