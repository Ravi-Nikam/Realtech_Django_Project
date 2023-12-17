from django.shortcuts import render,redirect
from .models import Account
from seller_Home_app.models import Product
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

#signup 
def signup(request):
	if request.method == "POST":
		print("============================>")
		try:
			Account.objects.get(Email=request.POST['Email'])
			return render(request,'signin.html')
		except:
			if request.POST['Password']==request.POST['Cpassword']:
				Account.objects.create(
					Name=request.POST['Name'],
					Mobile=request.POST['Mobile'],
					Email=request.POST['Email'],
					Password = make_password(request.POST['Password']),
					user = request.POST['Usertype'],
					Profile_picture = request.FILES["Profile_picture"]
				)
				msg = "User successfully Created !"
				return render(request,'signin.html',{'msg':msg})
			else:
				msg = "Password doesn't Match !"
				return render(request,'signin.html',{'msg':msg})
	return render(request,'signup_login.html')



def login(request):
	if request.method=="POST":
		try:
			user=Account.objects.get(Mobile=request.POST['Mobile'])
			print(user.user)
			checkpassword=check_password(request.POST.get('Password'),user.Password)
			if checkpassword==True:
				print(user.user)
				if user.user == 'Buyer':
					print(user.user)
					msg = "Welcome " + user.Name
					request.session['Name']=user.Name
					request.session['Email']=user.Email
					request.session['Profile_picture']=user.Profile_picture.url
					# product=Product.objects.all()
					return render(request,'index.html',{'msg':msg})
				else:
					try:
						msg = "Welcome " + user.Name
						print("msg",msg)
						request.session['Name']=user.Name
						request.session['Email']=user.Email
						request.session['Profile_picture']=user.Profile_picture.url
						return render(request,'seller-index.html',{'msg':msg,'user':user})
					except Exception as e:
						print("11111111111111111111111",e)
			else:
				msg = "Mobile number and password wrong !!"
				return render(request,'signin.html',{'msg':msg})
		except:
			msg = " Email and password does not match !! "
			return render(request,'signin.html',{'msg':msg})
	return render(request,'signin.html')

def logout(request):
	try:
		del request.session['Name']
		del request.session['Email']
		del request.session['Profile_picture']
		print("LOGOUT")
		return render(request,'index.html')
	except:
		return render(request,'index.html')
	
def Change_password(request):
	return render(request,'Change_password.html')