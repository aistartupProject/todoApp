# Generated by Django 5.0.7 on 2024-07-15 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creatd_at',
            new_name='created_at',
        ),
    ]
