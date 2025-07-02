from django.shortcuts import render, redirect
from crmapp.models import customer
from django.views.decorators. cache import cache_control
import datetime
from adminapp.models import Product
from . models import Response

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customerhome(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=customer.objects.get(emailaddress=userid)
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect("crmapp:login")
def logout(request):
        try:
            del request.session["userid"]
        except KeyError:
            return redirect("crmapp:loginuser")
        return redirect("crmapp:loginuser")
        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def response(request):
    try:
        if request.session['userid']!=None:
            cust=customer.objects.get(emailaddress=request.session['userid'])
            if request.method=="POST":
                name = cust.name
                contactno =cust.contactno
                emailaddress=cust.emailaddress
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                posteddate=datetime.datetime.today()
                res=Response(name=name,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype,subject=subject ,responsetext=responsetext,posteddate=posteddate)
                res.save()
                msg="Your response has been successfully recorded"
                return render(request,"response.html",{"msg":msg})
            return render(request,"response.html")
    except KeyError:
        return redirect("crmapp:login")
def viewprofile(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=customer.objects.get(emailaddress=userid)
            if request.method=="POST":
                name=request.POST["name"]
                gender=request.POST["gender"]
                address=request.POST["address"]
                contactno=request.POST["contactno"]
                emailaddress=request.POST["emailaddress"]
                customer.objects.filter(emailaddress=emailaddress).update(name=name,gender=gender,address=address,contactno=contactno)
                return redirect("customerapp:customerhome")
            return render(request,"viewprofile.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")

def dashboard(request):
    return render(request,"dashboard.html")

def dogs(request):
    return render(request,"dog.html")

def food(request):
    return render(request,"food.html")

def food1(request):
    return render(request,"food1.html")

def food2(request):
    return render(request,"food2.html")

def food3(request):
    return render(request,"food3.html")    

def food4(request):
    return render(request,"food4.html")

def food5(request):
    return render(request,"food5.html")

def food6(request):
    return render(request,"food6.html")

def food7(request):
    return render(request,"food7.html") 


def kid(request):
    return render(request,"kid.html")

def kid1(request):
    return render(request,"kid1.html")

def kid2(request):
    return render(request,"kid2.html")

def kid3(request):
    return render(request,"kid3.html")    

def kid4(request):
    return render(request,"kid4.html")

def kid5(request):
    return render(request,"kid5.html")

def kid6(request):
    return render(request,"kid6.html")

def kid7(request):
    return render(request,"kid7.html") 


def dfood(request):
    return render(request,"dfood.html")

def dfood1(request):
    return render(request,"dfood1.html")

def dfood2(request):
    return render(request,"dfood2.html")

def dfood3(request):
    return render(request,"dfood3.html")    

def dfood4(request):
    return render(request,"dfood4.html")

def dfood5(request):
    return render(request,"dfood5.html")




def dkid(request):
    return render(request,"dkid.html")

def dkid1(request):
    return render(request,"dkid1.html")

def dkid2(request):
    return render(request,"kid2.html")

def dkid3(request):
    return render(request,"dkid3.html")    

def dkid4(request):
    return render(request,"dkid4.html")

def dkid5(request):
    return render(request,"kid5.html")

def dkid6(request):
    return render(request,"dkid6.html")

def dkid7(request):
    return render(request,"dkid7.html")

def dkid8(request):
    return render(request,"dkid8.html")

def dkid9(request):
    return render(request,"dkid9.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def products(request):
    try:
        if request.session["userid"]!=None:
            userid=request.session["userid"]
            cust=customer.objects.get(emailaddress=userid)
            prod=Product.objects.all()
            return render(request,"products.html",locals())
    except KeyError:
        return redirect("crmapp:login")