from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('registration/',views.registration,name='registration'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('cat/',views.cat,name='cat'),
    path('dogs/',views.dogs,name='dogs'),
    path('search/',views.search,name='search'),
]
