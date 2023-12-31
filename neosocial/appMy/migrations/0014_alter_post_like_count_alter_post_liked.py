# Generated by Django 4.2.1 on 2023-08-27 17:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0013_post_like_count_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Beğen sayısı'),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(related_name='liked_post', to=settings.AUTH_USER_MODEL, verbose_name='Beğenenler'),
        ),
    ]
