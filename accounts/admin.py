# from django.contrib import admin

# from .models import CustomUserModel

# admin.site.register(CustomUserModel)
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    list_display = ('id', 'email')
    ordering = ('id',)