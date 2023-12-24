from django.db import models

user_type=(('Buyer','Buyer'),
           ('Seller','Seller'))

# Create your models here.
class Account(models.Model):
    Name = models.CharField(max_length=25)
    Mobile = models.PositiveBigIntegerField()
    Email = models.EmailField(unique=True, max_length=100,primary_key=True)
    Password = models.CharField(max_length=30)
    Profile_picture = models.ImageField(default="",upload_to='Profile_picture/')
    user = models.CharField(max_length=15,choices=user_type)

    def __str__(self):
        return self.user + " " + self.Name
    
# class wishlist(models.Model):
#     account = models.ForeignKey(Account,on_delete=models.CASCADE)
#     product = models.ForeignKey("Product", on_delete=models.SET_NULL,null=True,blank=True)
#     class Meta:
#         unique_together = ("account","product")  # multiple entries allowed for same account and different products
#         unique_together = ("account","product")  # multiple users can add same product to their wishlist
