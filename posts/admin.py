from dataclasses import field
from django.contrib import admin
from . import models

# Register your models here.


class CommentInline(admin.TabularInline):
    model = models.Comment


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created")
    list_filter = ("category",)


@admin.register(models.QnA)
class InquiryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("기본정보", {"fields": ("title", "contents", "writer","email", "message")}),
        ("부가정보", {"fields": ("is_phone", "is_email")}),
        ("기타", {"fields": ("category", "status")}),
    )
    list_display = (
        "title",
        "created",
        "category",
        "status",
        "is_email",
        "is_phone",
    )
    list_filter = ("category",)
    search_fields = ["title", "email", "message"]
    inlines = (CommentInline,)
