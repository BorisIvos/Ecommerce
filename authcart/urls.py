from django.urls import path 
from authcart import views 

urlpatterns = [
    path('singup/',views.singup,name='singup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
]
