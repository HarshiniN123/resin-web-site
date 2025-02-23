# Generated by Django 5.0.6 on 2024-07-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resin_app', '0009_alter_orders_resin_alter_orders_wooden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='keychain',
            field=models.CharField(choices=[('M', 'Photo Placed Agate Keychain'), ('N', 'Photo Placed Round Keychain'), ('O', 'Photo Placed Heart Keychain'), ('P', 'Photo Placed Rectangle Keychain'), ('U', 'Photo Placed Square Keychain'), ('Q', 'Baby Feet Keychain'), ('R', 'Alphabet Keychain'), ('S', 'Spotify Keychain'), ('T', 'None')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='resin',
            field=models.CharField(choices=[('A', 'Four Inch Agate Frame'), ('B', 'Four Inch Round Frame'), ('C', 'Four Inch Heart Frame'), ('D', 'Six Inch Agate Frame'), ('E', 'Six Inch Round Frame'), ('F', 'Twelve Inch Agate Frame'), ('G', '12x9 Inch Agate Frame'), ('H', '8 Inch Agate Frame'), ('V', 'None')], max_length=100),
        ),
    ]
