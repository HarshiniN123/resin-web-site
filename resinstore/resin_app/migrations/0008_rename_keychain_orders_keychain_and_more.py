# Generated by Django 5.0.6 on 2024-07-08 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resin_app', '0007_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Keychain',
            new_name='keychain',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Resin',
            new_name='resin',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='Wooden',
            new_name='wooden',
        ),
    ]
