# Generated by Django 4.2.7 on 2023-12-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0002_wishlist_delete_edit_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='Iswishlist',
            field=models.BooleanField(default=False),
        ),
    ]