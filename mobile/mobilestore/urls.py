from django.urls import path
from .views import home,index,about,services,contact,userform,evenodd,marksheet,calculator,login
urlpatterns = [
    path('',home,name="home"),
    path('index/',index,name="index"),
    path('about/',about,name="about"),
    path('services/',services,name="services"),
    path('contact/',contact,name="contact"),
    path('userform/',userform,name="userform"),
    path('evenodd',evenodd,name="evenodd"),
    path('marksheet',marksheet,name="marksheet"),
    path('calculator',calculator,name="calculator"),
    path('login',login,name="login")
    ]