from django.urls import path
from . import views
urlpatterns = [
    path('Seller_home/',views.Seller_home,name="Seller_home"),      
    path('Add_products/',views.Add_products,name="Seller_add_products"),      
    path('Seller_view_product/',views.Seller_view_product,name="Seller_view_product")
]