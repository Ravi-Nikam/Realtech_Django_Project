from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home_page"),   
    # path('Products/',views.products,name="Products"),   
    path('Blog/',views.blog,name="Blog"),   
    path('About/',views.about,name="About"),   
    path('Contact_us/',views.contact_us,name="Contact_us"),   
    path('Profile/',views.Profile,name="Profile"),   
    path('All_products/',views.All_products,name="All_products"),
    path('Product_description/<str:pk>/',views.Product_description,name="Product_description")
]