from django.contrib.auth.models import update_last_login
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('cart/',views.cart,name="cart"),
    path('update_item/',views.updateItem,name='update_item'),
    path('checkout/',views.checkout,name='checkout'),
    path('order/',views.processOrder,name='order'),


]
