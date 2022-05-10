from django.db import models

# Create your models here.


class FAQ(models.Model):

    CATEGORY_NORMAL = "일반"
    CATEGORY_USERS = "계정"
    CATEGORY_ETC = "기타"
    CATEGORY_CHOICE = (
        (CATEGORY_NORMAL, "일반"),
        (CATEGORY_USERS, "계정"),
        (CATEGORY_ETC, "기타"),
    )

    created = models.DateTimeField(auto_now_add=True)  # 생성일자
    updated = models.DateTimeField(auto_now=True)  # 수정일자
    contents = models.TextField(verbose_name="내용")
    title = models.CharField(max_length=50, verbose_name="제목")
    category = models.CharField(
        max_length=12,
        choices=CATEGORY_CHOICE,
        default=CATEGORY_NORMAL,
        verbose_name="카테고리",
    )
    comment = models.ForeignKey(
        "Comment",
        related_name="FAQ",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name="댓글",
    )

    class Meta:
        verbose_name_plural = "자주묻는질문"

    def __str__(self):
        return self.title


class QnA(models.Model):

    STATUS_PENDING = "문의등록"
    STATUS_CONFIRMED = "접수완료"
    STATUS_ANSWERED = "답변완료"

    STATUS_CHOICE = (
        (STATUS_PENDING, "문의등록"),
        (STATUS_CONFIRMED, "접수완료"),
        (STATUS_ANSWERED, "답변완료"),
    )
    CATEGORY_NORMAL = "일반"
    CATEGORY_USERS = "계정"
    CATEGORY_ETC = "기타"
    CATEGORY_CHOICE = (
        (CATEGORY_NORMAL, "일반"),
        (CATEGORY_USERS, "계정"),
        (CATEGORY_ETC, "기타"),
    )
    Is_true = True
    Is_False = False
    Is_choice = ((Is_true, "예"), (Is_False, "아니요"))
    created = models.DateTimeField(auto_now_add=True)  # 생성일자
    updated = models.DateTimeField(auto_now=True)  # 수정일자
    title = models.CharField(max_length=50, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    message = models.IntegerField(verbose_name="번호")
    is_phone = models.BooleanField(
        default=Is_False,
        blank=True,
        null=True,
        choices=Is_choice,
        verbose_name="핸드폰 수신",
    )
    is_email = models.BooleanField(
        default=Is_False,
        blank=True,
        null=True,
        choices=Is_choice,
        verbose_name="이메일 수신",
    )
    email = models.EmailField(max_length=100, verbose_name="이메일")
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING, verbose_name="상태"
    )
    category = models.CharField(
        max_length=12,
        choices=CATEGORY_CHOICE,
        default=CATEGORY_NORMAL,
        verbose_name="카테고리",
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

    class Meta:
        verbose_name_plural = "답변"
