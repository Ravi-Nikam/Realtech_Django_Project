from django.db import models
from django.utils import timezone
from Account.models import Account
from seller_Home_app.models import Product
# Create your models here.
class Wishlist(models.Model):
    User=models.ForeignKey(Account,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    # Iswishlist = models.BooleanField(default=False)

    def __str__(self):
        return self.Product.Product_name
    
class Cart(models.Model):
    User=models.ForeignKey(Account,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Order_date = models.DateTimeField(default=timezone.now)
    Payment_status = models.BooleanField(default=False)
    Total_amount = models.PositiveIntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)
