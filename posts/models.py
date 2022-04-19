from django.db import models

# Create your models here.


class Categories(models.Model):
    cate = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "카테고리"

    def __str__(self):
        return f"{self.cate}"


class QnA(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # 생성일자
    updated = models.DateTimeField(auto_now=True)  # 수정일자
    title = models.CharField(max_length=50, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    message = models.IntegerField()
    email = models.EmailField(max_length=100)
    category = models.ForeignKey(
        "Categories",
        related_name="QnA",
        on_delete=models.DO_NOTHING,
        verbose_name="카테고리",
        null=True,
        blank=True,
    )
    comment = models.ManyToManyField(
        "Comment", related_name="QnA", blank=True, verbose_name="댓글"
    )

    class Meta:
        verbose_name_plural = "문의사항"

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=300)
