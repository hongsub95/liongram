from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Categories)
class CategoryAdmin(admin.ModelAdmin):
    field = "cate"
    ordering = ["cate"]


@admin.register(models.QnA)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "category", "comment")

    def comment(self, obj):
        c = obj.comment.all()
        comment_list = list()
        for co in c:
            comment_list.append(co)
        return len(comment_list)
