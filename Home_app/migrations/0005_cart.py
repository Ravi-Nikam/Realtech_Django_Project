# Generated by Django 4.2.7 on 2023-12-23 18:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seller_Home_app', '0008_alter_product_product_name'),
        ('Account', '0004_rename_profile_picture_account_profile_picture'),
        ('Home_app', '0004_remove_wishlist_iswishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Payment_status', models.BooleanField(default=False)),
                ('Total_amount', models.PositiveIntegerField()),
                ('quantity', models.IntegerField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller_Home_app.product')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.account')),
            ],
        ),
    ]