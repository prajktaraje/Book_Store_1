from django.contrib import admin

# Register your models here.

from .models import Book

# Register your models here.
@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Author','Title')
