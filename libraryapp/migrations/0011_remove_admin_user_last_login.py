# Generated by Django 5.0.7 on 2025-01-13 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0010_admin_user_is_active_admin_user_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_user',
            name='last_login',
        ),
    ]
