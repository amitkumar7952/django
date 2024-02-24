# Create your views here.
from django.shortcuts import render
# Create your views here.
def home(request):
    return render (request,"home.html")
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    services= Services.objects.all().order_by('services_title')
    if request.method=="GET":
        st= request.GET.get('servicesname')
        if st!= None:
            services= Services.objects.filter(service_title_icont)
            data={
                "ser": services
            }
        return render(request,"services.html",data) 
def contact(request):
    if request.method== "POST":
        nm= request.POST.get('Name')
        em= request.POST.get('Email')
        pnum= request.POST.get('Phone')
        msg= request.POST.get('Messages')
        print(">>>>>>", nm, em, pnum, msg)
        user = Contact(name=nm, email=em, phone=pnum, messages=msg)
        user.save()
        return render(request,"contact.html")
    def userform(request):
        final_output=0
        try:
            if request.method=="GET":
                n1= int(request.GET['Value1'])
                n2= int(request.GET['Value2'])
                final_output=n1+n2
                print(final_output)
                except:
                pass
            return render(request,"userform.html",{'output':final_output})
    def evenodd(request):
        c=""
        if request.method=="POST":
            Value1=int(request.POST.get("Value1"))
            if Value1%2==0:
                c="Even"
            else:
                c="Odd"
        return render(request,"evenodd.html",{'output':c})
    def marksheet(request):
        return render(request,"marksheet.html")
    def calculator(request):
        return render(request,"calculator.html")
    def login(request):
        return render(request,"login.html")
    