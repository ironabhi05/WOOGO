from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('event/',views.event),
    path('signout/',views.signout),
    path('product/',views.mproduct),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('myprofile/',views.myprofile),
    path('mycart/',views.mycart),
    path('cartitems/',views.cartitems),
    path('order/',views.morder),
    path('indexcart/',views.indexcart),
    path('instagram/',views.insta),
    path('orderslist/',views.orderslist),
    path('profile/',views.profile)
]