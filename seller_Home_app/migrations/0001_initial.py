# Generated by Django 4.2.7 on 2023-12-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0004_rename_profile_picture_account_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=25)),
                ('Product_Price', models.PositiveIntegerField()),
                ('Product_category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('kids', 'kids')], max_length=20)),
                ('Product_brand', models.CharField(choices=[('Levis', 'Levis'), ('pape', 'pape'), ('Danieam', 'Danieam')], max_length=20)),
                ('Product_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=20)),
                ('Product_image', models.ImageField(upload_to='Product_image/')),
                ('Product_description', models.TextField(max_length=100)),
                ('seller_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.account')),
            ],
        ),
    ]
