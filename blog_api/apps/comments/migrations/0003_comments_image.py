# Generated by Django 4.1.4 on 2023-10-15 13:39

import apps.comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comments_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.comments.models.upload_to),
        ),
    ]