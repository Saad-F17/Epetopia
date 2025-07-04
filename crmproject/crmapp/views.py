from django.shortcuts import render, redirect
from . models import Enquiry , customer , login
#from django.core.exceptions import ObjectDoesExist
from django.core.exceptions import ObjectDoesNotExist
import datetime


# Create your views here.
def index(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"aboutus.html")
def registration(request):
    if request.method=="POST":
        name=request.POST["name"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        password=request.POST["password"]
        regdate=datetime.datetime.today()
        cus=customer(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress ,regdate=regdate)
        cus.save()
        log=login(userid=emailaddress,password=password,usertype="customer")
        log.save()
        return render(request,"registration.html",{"msg":"registration is done"})
    return render(request,"registration.html")

def loginuser(request):
    if request.method=="POST":
        userid=request.POST["userid"]
        password=request.POST["password"]
        try:
            obj=login.objects.get(userid=userid,password=password)
            if obj is not None:
                    if obj.usertype=='customer':
                        request.session["userid"]=userid
                        return redirect("customerapp:customerhome")
                    elif obj.usertype=='admin':
                        request.session["adminid"]=userid
                        return redirect("adminapp:adminhome")
        except ObjectDoesNotExist:
            msg="Invalid User"
        return render(request,"login.html",{"msg":msg})
    return render(request,"login.html")

def contactus(request):
    if request.method=="POST":
        name=request.POST["name"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        posteddate=datetime.datetime.today()
        enq=Enquiry(name=name,contactno=contactno,emailaddress=emailaddress,subject=subject,message=message,posteddate=posteddate)
        enq.save()
        return render(request,"contactus.html",{"msg":"Enquiry is saved"})
    return render(request,"contactus.html")
def cat(request):
    return render(request,"cat.html")

def dogs(request):
    return render(request,"dogs.html")

def search(request):
    if request.method=="POST":
        page=request.POST['page']
        page=page+".html"
        return render(request,page)
    return render(request,"index.html")
    