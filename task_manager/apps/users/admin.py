from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ('id',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff',
                    'date_joined')
    list_display_links = ('id',)
    search_fields = ('username',)


admin.site.register(User, MyUserAdmin)
