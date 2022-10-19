from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from recipes.admin import Admin
from users.models import Follower, User


class AdminForUser(UserAdmin):
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

class FollowerAdmin(Admin):
    list_display = ('user', 'author')
    list_filter = ('user',)


admin.site.register(User, AdminForUser)
admin.site.register(Follower, FollowerAdmin)
