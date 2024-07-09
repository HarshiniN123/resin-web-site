from django.urls import path
from resin_app import views

urlpatterns = [
    path('',views.front),
    path('signup', views.user_signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('home', views.home, name='home'),
    path('products',views.products,name='products'),
    path('orders',views.orders,name='customize'),
    path('discount',views.discount,name='discount'),
    path('about',views.about,name='about'),
    path('stand',views.stand,name='stand'),
    path('shipping',views.shipping,name='shipping'),
    path('logout', views.user_logout, name='logout'),
    path('name',views.order,name='name')
    
]