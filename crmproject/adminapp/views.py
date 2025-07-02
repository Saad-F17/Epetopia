from django.shortcuts import render ,redirect
from django.views.decorators.cache import cache_control
from crmapp.models import customer,Enquiry,login
from . models import Product
from customerapp.models import Response



# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminhome (request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render(request,"adminhome.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")
def logout(request):
        try:
            del request.session["adminid"]
            return redirect("crmapp:loginuser")
        except KeyError:
            return redirect("crmapp:loginuser")
        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcustomers(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust=customer.objects.all()
            return render(request,"viewcustomers.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewenquires (request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            enq=Enquiry.objects.all()
            return render(request,"viewenquires.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")
        
def delenq(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("adminapp:viewenquires")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            if request.method=="POST":
                productname=request.POST['productname']
                mfgdate=request.POST['mfgdate']
                expdate=request.POST['expdate']
                price=request.POST['price']
                productpic=request.FILES['productpic']
                prd=Product(productname=productname,mfgdate=mfgdate,expdate=expdate,price=price,productpic=productpic)
                prd.save()
                msg='Product id added'
                return render(request,"product.html",locals())
            return render(request,"product.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcomplaints (request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            comp = Response.objects.filter(responsetype='Complaint')
            return render(request,"viewcomplaints.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewfeedback (request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            feed = Response.objects.filter(responsetype='Feedback')
            return render(request,"viewfeedback.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")

def delfeed(request,id):
    Response.objects.get(id=id).delete()
    return redirect("adminapp:viewfeedback")
def delcomp(request,id):
    Response.objects.get(id=id).delete()
    return redirect("adminapp:viewcomplaints")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword (request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render(request,"changepassword.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")

def delprod(request,pid):
    Product.objects.get(pid=pid).delete()
    return redirect("adminapp:viewproducts")





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewproducts (request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            prod=Product.objects.all()
            return render(request,"viewproducts.html",locals())
    except KeyError:
        return redirect("crmapp:loginuser")