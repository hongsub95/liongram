from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created")
    list_filter = ("category",)


@admin.register(models.QnA)
class InquiryAdmin(admin.ModelAdmin):
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

    def comment(self, obj):
        c = obj.comment.all()
        comment_list = list()
        for co in c:
            comment_list.append(co)
        return len(comment_list)
