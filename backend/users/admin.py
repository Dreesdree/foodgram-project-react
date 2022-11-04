from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import FollowAuthor, User


class AdminForUser(UserAdmin):
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class FollowAuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')
    search_fields = ('user__username', 'author__username')




admin.site.register(User, AdminForUser)
admin.site.register(FollowAuthor, FollowAuthorAdmin)
