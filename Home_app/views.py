from django.shortcuts import render,redirect
from Account.models import Account
from seller_Home_app.models import Product
from .models import Wishlist,Cart
# Create your views here.
def index(request):
    return render(request,'index.html')
    # if request.session['Email'] == None:
    #     # Products=Product.objects.all()
    #     return render(request,'index.html')
    # else:
    #     user = Account.objects.get(email=request.session['Email'])
    #     if user.user == 'Seller':
    #         return render(request,'seller-index.html')
    # return render(request,'index.html')

def Profile(request):
    user=Account.objects.get(Email=request.session['Email'])
    if request.method == "POST":
        user.Name = request.POST['Name']
        user.Mobile=request.POST['Mobile']
        user.Email=request.POST['Email']
        try:
            user.Profile_picture=request.FILES['Profile_picture']
        except Exception as e:
            print("ERRRP",e)
        user.save()
        request.session['Profile_picture'] = user.Profile_picture.url
        msg = "Profile updated Successfully "
        if user.user == "Buyer":
            return render(request,'Profile.html',{'user':user,'msg':msg})
        else:
            return render(request,'seller-profile.html',{'user':user,'msg':msg})
    else:
        if user.user == "Buyer":
            return render(request,'Profile.html',{'user':user})
        else:
            return render(request,'seller-profile.html',{'user':user})


def Product_description(request,pk):
    # user = Account.objects.get(id=pk)
    product_details=Product.objects.get(id=pk)
    return render(request,'Product_description.html',{'Product_details':product_details})

def Add_to_wishlist(request,pk):
    user = Account.objects.get(Email = request.session['Email'])
    product = Product.objects.get(id=pk)
    Wishlist.objects.create(User=user,Product=product)
    product.Iswishlist = True
    product.save()
    return redirect('Product_description',pk=product.id)

def view_wishlist(request):
    user=Account.objects.get(Email=request.session['Email'])
    try:
        wishlist_info=Wishlist.objects.filter(User=user)
        print(wishlist_info)
    except Exception as e:
        print("Error in getting wishlist info : ",e)
    return render(request,'View_to_wishlist.html',{'wishlist_info':wishlist_info})

def Remove_to_wishlist(request,pk):
    product = Product.objects.get(id=pk)
    product.Iswishlist = False
    product.save()
    user = Account.objects.get(Email = request.session['Email'])
    wishlist=Wishlist.objects.get(User=user,Product=product)
    wishlist.delete()
    return redirect('Product_description',pk=product.id)

def Add_to_cart(request,pk):
    user=Account.objects.get(Email = request.session['Email'])
    product = Product.objects.get(id=pk)
    try:
        Cart.objects.create(User = user,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                            Product=product,
                            quantity=1,
                            Total_amount=product.Product_price,
                            Payment_status=False)
    except Exception as  e:
        print("Cart Might be a issue !",e)
    product.Iscart = True
    product.save()
    return redirect('Product_description',pk=product.id)

def view_cart(request):
    user=Account.objects.get(Email=request.session['Email'])
    try:
        cart_info=Cart.objects.filter(User=user)
        print(cart_info)
    except Exception as e:
        print("Error in getting cart info : ",e)
    return render(request,'shoping-cart.html',{'cart_info':cart_info})

def Remove_to_cart(request,pk):
    product = Product.objects.get(id=pk)
    product.Iscart = False
    product.save()
    user = Account.objects.get(Email = request.session['Email'])
    cart=Cart.objects.get(User=user,Product=product)
    cart.delete()
    return redirect('Product_description',pk=product.id)


def change_quality(request,pk):
    product = Product.objects.get(id=pk)
    quality = int(request.POST.get('quantity'))
    print("quality is **********************************>",quality)
    total_amount = int(quality) * int(product.Product_price)
    print("total amount",total_amount)
    return render(request,'shoping-cart.html',{'total_amount':total_amount})

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact.html')

def Edit_menu(request):
    return render()

def All_products(request):
    Products=Product.objects.all()
    return render(request,"All_products.html",{"Product":Products})