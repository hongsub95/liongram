# Generated by Django 4.0.4 on 2022-04-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_categories_rename_content_qna_contents_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qna',
            options={'verbose_name_plural': '문의사항'},
        ),
        migrations.AlterField(
            model_name='qna',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, related_name='QnA', to='posts.comment', verbose_name='댓글'),
        ),
    ]