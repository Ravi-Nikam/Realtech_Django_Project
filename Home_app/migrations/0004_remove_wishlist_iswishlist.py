# Generated by Django 4.2.7 on 2023-12-23 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0003_wishlist_iswishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='Iswishlist',
        ),
    ]
