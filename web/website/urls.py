from django.urls import path
from .views import home,about,loginuser,contact,evenodd,userform,services,signup,logoutuser

urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('login/',loginuser,name="loginuser"),
    path('contact/',contact,name="contact"),
    path('evenodd/',evenodd,name="evenodd"),
    path('userform/',userform,name="userform"),
    path('services/',services,name="services"),
    path('signup/',signup,name="signup"),
    path('logout/',logoutuser,name="logout"),
]