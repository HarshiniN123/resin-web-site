# Generated by Django 5.0.6 on 2024-07-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resin_app', '0010_alter_orders_keychain_alter_orders_resin'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
