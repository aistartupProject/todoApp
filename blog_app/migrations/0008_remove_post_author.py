# Generated by Django 5.0.7 on 2024-07-15 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
