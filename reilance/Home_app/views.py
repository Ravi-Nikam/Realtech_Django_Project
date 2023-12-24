from django.shortcuts import render,redirect
from Account.models import Account
from seller_Home_app.models import Product
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
    product_details=Product.objects.get(id=pk)
    print("==========>",product_details.Product_size)
    print("==========>",product_details.Product_name)
    print("]]]]]]]]]]]]]]]]]]",product_details)
    return render(request,'Product_description.html',{'Product_details':product_details})

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