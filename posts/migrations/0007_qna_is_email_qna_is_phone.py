# Generated by Django 4.0.4 on 2022-05-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_qna_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='is_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='qna',
            name='is_phone',
            field=models.BooleanField(default=False),
        ),
    ]
