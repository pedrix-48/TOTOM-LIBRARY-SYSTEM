# Generated by Django 5.0.7 on 2025-05-25 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0006_remove_staff_password_remove_staff_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='admin_user',
            name='username',
        ),
    ]
