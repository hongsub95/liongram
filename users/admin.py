from atexit import register
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ("기본정보", {
            'fields': ("username","gender","first_name","bio"
            ),
        }),
        ("부가정보",{"fields":("phone","birthday")}),
        ("기타",{"fields":("superhost",)})
    )
    list_display = (
        "username",
        "birthday",
        "phone",
    )
