from django.db import models

# Create your models here.


class Categories(models.Model):
    cate = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "카테고리"

    def __str__(self):
        return f"{self.cate}"


class QnA(models.Model):

    STATUS_PENDING = "pending"  # 문의등록
    STATUS_CONFIRMED = "confirmed"  # 접수완료
    STATUS_ANSWERED = "answered"  # 답변완료

    STATUS_CHOICE = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_ANSWERED, "answered"),
    )
    created = models.DateTimeField(auto_now_add=True)  # 생성일자
    updated = models.DateTimeField(auto_now=True)  # 수정일자
    title = models.CharField(max_length=50, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    message = models.IntegerField()
    is_phone = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING, verbose_name="상태"
    )
    category = models.ForeignKey(
        "Categories",
        related_name="QnA",
        on_delete=models.DO_NOTHING,
        verbose_name="카테고리",
        null=True,
        blank=True,
    )
    comment = models.ManyToManyField(
        "Comment",
        related_name="QnA",
        blank=True,
        verbose_name="댓글",
    )

    class Meta:
        verbose_name_plural = "문의사항"

    def __str__(self):
        return self.title


class Comment(models.Model):
    qna = models.ForeignKey(
        "QnA",
        related_name="Comment",
        null=True,
        blank=True,
        verbose_name="게시글",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=300)
