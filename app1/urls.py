from atexit import register
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home),
    path('home.html',views.home,name="home"),
    path('story.html/',views.story,name="story"),
    path('product.html',views.product,name="product"),
    path('milk.html',views.milk,name="milk"),
    path('bread.html',views.bread,name="bread"),
    path('register.html/',views.register,name="register"),
    path('login.html/',views.login,name="login"),
    path('cart.html/',views.cart,name="cart"),
]
