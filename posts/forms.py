from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["comment"]


class CategoryForm(forms.ModelForm):
    CATEGORY_NORMAL = "일반"
    CATEGORY_USERS = "계정"
    CATEGORY_ETC = "기타"
    CATEGORY_CHOICE = (
        (CATEGORY_NORMAL, "일반"),
        (CATEGORY_USERS, "계정"),
        (CATEGORY_ETC, "기타"),
    )
    category = forms.ChoiceField(choices=CATEGORY_CHOICE, label="카테고리")

    class Meta:
        model = models.QnA
        fields = ["category"]
