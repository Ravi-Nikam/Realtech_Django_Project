from django.db import models
from Account.models import Account
# Create your models here.
class Product(models.Model):
    category = (
        ("Men","Men"),("Women","Women"),("kids","kids")
    )
    brand = (
        ('Levis',"Levis"),('pape',"pape"),('Danieam',"Danieam")
    )
    size=(
        ('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL')
    )
    seller_key= models.ForeignKey(Account,on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=150)
    Product_price = models.PositiveIntegerField()
    Product_category = models.CharField(max_length=20,choices=category)
    Product_brand = models.CharField(max_length=20,choices=brand)
    Product_size = models.CharField(max_length=20,choices=size)
    Product_image = models.ImageField(upload_to='Product_image/')
    Product_description = models.TextField(max_length=250)
    Iswishlist = models.BooleanField(default=False)
    Iscart=models.BooleanField(default=False)

    def __str__(self):
        print(self.Product_brand)
        return  str(self.Iswishlist) + " " +str(self.Product_name)