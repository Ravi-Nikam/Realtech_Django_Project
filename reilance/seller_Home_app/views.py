from django.shortcuts import render,redirect
from .models import Product,Account
# Create your views here.
def Seller_home(request):
    return render(request,'seller-index.html')

def Add_products(request):
    seller = Account.objects.get(Email=request.session['Email'])
    try:
        if request.method == "POST":
            Product.objects.create(
                    seller_key = seller,
                    Product_image=request.FILES['Seller_product_picture'],
                    Product_name=request.POST['Product_name'],
                    Product_price=request.POST['Product_price'],
                    Product_category=request.POST.get('Product_category'),
                    Product_size=request.POST.get('Product_size'),
                    Product_brand=request.POST.get('Product_brand'),
                    Product_description=request.POST['Product_description']
            )
        msg="Product Added Successfully !!"
        return render(request,'seller-add_product.html',{'msg':msg})
    except Exception as e:
        print("Exception",e)
        msg = "Product Not Added"
        return render(request,'seller-add_product.html',{'msg':msg})

def Seller_view_product(request):
    try:
        Seller_email=Account.objects.get(Email=request.session['Email'])        
        Products=Product.objects.filter(seller_key=Seller_email)
        return render(request,'Seller_view_product.html',{'Products':Products})
    except Exception as e:
        msg = "No Product Found !!"
        return render(request,'Seller-index.html',{'msg':msg})


def seller_profile(request): 
    return render(request,'seller-profile.html')


