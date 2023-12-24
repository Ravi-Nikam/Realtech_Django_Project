from django.urls import path
from . import views
urlpatterns = [
    path('Seller_home/',views.Seller_home,name="Seller_home"),      
    path('Add_products/',views.Add_products,name="Seller_add_products"),      
    path('Seller_view_product/',views.Seller_view_product,name="Seller_view_product"),
    path('Seller_details_product/<int:pk>/',views.Seller_details_product,name="Seller_details_product"),
    path('Edit_products/<int:pk>/',views.Edit_products,name="Edit_products"),      
    path('Update_product_details/<int:pk>/',views.Update_product_details,name="Update_product_details"),
    path('Delete_products/<int:pk>/',views.Delete_products,name="Delete_products"), 
]