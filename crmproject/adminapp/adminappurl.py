from django.urls import path
from . import views


urlpatterns=[
    path('adminhome/', views.adminhome, name="adminhome"),
    path('logout/', views.logout, name="logout"),
    path('viewcustomers/', views.viewcustomers, name="viewcustomers"),
    path('viewenquires/', views.viewenquires, name="viewenquires"),
    path('delenq/<id>', views.delenq, name="delenq"),
    path('product/', views.product, name="product"),
    path('viewcomplaints/', views.viewcomplaints, name="viewcomplaints"),
    path('viewfeedback/', views.viewfeedback, name="viewfeedback"),
    path('delfeed/<id>', views.delfeed, name="delfeed"),
    path('delcomp/<id>', views.delcomp, name="delcomp"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('viewproducts/', views.viewproducts, name="viewproducts"),
    path('delprod/<pid>', views.delprod, name="delprod"),

]