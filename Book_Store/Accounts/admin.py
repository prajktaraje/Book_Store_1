from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ['username', 'Contact_number','first_name','last_name','email','password']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('Contact_number',)}),
    ) #this will allow to change these fields in admin module


admin.site.register(User, MyUserAdmin)

