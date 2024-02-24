from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Services
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def home(request):
    return render(request,"home.html")
def footer(request):
    return render(request,"footer.html")
def about(request):
    return render(request,"about.html")
def loginuser(request):
    if request.method=='POST':
        
        eml = request.POST.get('usr')
        pwd = request.POST.get('pwd')

        user = authenticate(request, username=eml, password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'login.html',{})
def contact(request):
    if request.method=="POST":
        nm= request.POST.get('name')
        em= request.POST.get('email')
        pnum= request.POST.get('phone')
        msg= request.POST.get('message')
        print(">>>",nm,em,pnum,msg)
        user = Contact(name=nm,email=em,phone=pnum,message=msg)
        user.save()
    return render(request,"contact.html")
def evenodd(request):
    c=""
    if request.method=="POST":
        Value1=int(request.POST.get("Value"))
        if Value1%2==0:
            c="Even"
        else:
            c="Odd"
    return render(request,"evenodd.html",{'output':c})
def userform(request):
    final_output=0
    try:
        if request.method=="GET":
            n1=int(request.GET['Value1'])
            n2=int(request.GET['Value2'])
            final_output=n1+n2
            print(final_output)
    except:
        pass
    return render(request,"userform.html",{'output':final_output})
def services(request):
    services= Services.objects.all().order_by('service_title')
    if request.method=="GET":
        st= request.GET.get('servicename')
        if st!= None:
            services= Services.objects.filter(service_title=st)
            data={
                "ser": services
            }
            return render(request,"services.html",data)
    return render(request,"services.html",{"ser": services})
def signup(request):
    frm=UserCreationForm()
    if request.method=='POST':
        frm=UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('signup')
    return render(request,"signup.html",{'fm':frm})
def logoutuser(request):
    logout(request)
    return redirect('loginuser')