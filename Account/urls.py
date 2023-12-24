from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name="Sign-up"),   
    path('Login/',views.login,name="Login"), 
    path('Logout/',views.logout,name="Logout"), 
    path('Change_password/',views.Change_password,name="Change_password"), 
]