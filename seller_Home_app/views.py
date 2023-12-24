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
    
def Seller_details_product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'Seller_Product_description.html',{"Product_details":product})

def Edit_products(request,pk):
    Product_info=Product.objects.get(id=pk)
    print(Product_info)
    return render(request,'Seller_Edit_products.html',{'Product_info':Product_info})

def Update_product_details(request,pk):
    try:
        if request.method=='POST':
            try:
                Product_pk=Product.objects.get(id=pk)
                print(Product_pk)
            except Exception as e:
                print("Product Details didn't get it ")
            Product_pk.Product_name=request.POST['Product_name']
            Product_pk.Product_price=request.POST['Product_price']
            Product_pk.Product_category=request.POST['Product_category']
            Product_pk.Product_brand=request.POST['Product_brand']
            Product_pk.Product_size=request.POST['Product_size']
            Product_pk.Product_description=request.POST['Product_description']                
            try:
                Product_pk.Product_image=request.FILES['Product_image']
            except Exception as e:
                pass
            Product_pk.save()
            msg = "Product Update successfully"
            return render(request,'Seller_Edit_products.html',{'Product_info':Product_pk,'msg':msg})
        else:
            return render(request,'Seller_Edit_products.html')        
    except Exception as e:
        print("fatching error")        
    return render(request,'Seller_Edit_products.html')
        

def Delete_products(request,pk):
    Product_remove=Product.objects.get(id=pk)
    Product_remove.delete()
    msg = "Successfully product removed !!"
    return render(request,'Seller_view_product.html',{'msg':msg})

def seller_profile(request): 
    return render(request,'seller-profile.html')


