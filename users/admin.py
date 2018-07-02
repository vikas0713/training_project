from django.contrib import admin

from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	"""
	Profile Admin interface changes
	"""
	list_display = ['id', 'username', 'email', 'is_superuser']
	search_fields = ["username", "email"]


admin.site.register(Profile, ProfileAdmin)