# Generated by Django 4.0.4 on 2022-05-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment_qna_alter_qna_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('answered', 'answered')], default='pending', max_length=12),
        ),
    ]
