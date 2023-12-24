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
    path('Product_description/<str:pk>/',views.Product_description,name="Product_description"),
    path('Add_to_wishlist/<int:pk>/',views.Add_to_wishlist,name="Add_to_wishlist"),
    path('View_wishlist/',views.view_wishlist,name="View_wishlist"),
    path('Remove_to_wishlist/<int:pk>/',views.Remove_to_wishlist,name="Remove_to_wishlist"),
    path('Add_to_cart/<int:pk>/',views.Add_to_cart,name="Add_to_cart"),
    path('view_cart/',views.view_cart,name="view_cart"),
    path('Remove_to_cart/<int:pk>/',views.Remove_to_cart,name="Remove_to_cart"),
    path('change_quality/<int:pk>/',views.change_quality,name="change_quality"),
]