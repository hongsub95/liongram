from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, ("Male")),
        (GENDER_FEMALE, ("Female")),
        (GENDER_OTHER, ("Other")),
    )

    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name="아이디")
    birthday = models.DateField(null=True, blank=True, verbose_name="생년월일")
    phone = models.CharField(max_length=12, verbose_name="전화번호")
    gender = models.CharField(
        ("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    )

    bio = models.TextField(("bio"), blank=True)
    superhost = models.BooleanField(default=False)
