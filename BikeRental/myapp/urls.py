from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home-page'),
    path('about',views.about, name='about-page'),
    path('services',views.services, name='services-page'),
    path('review',views.review, name='review-page'),
    path('contactus',views.contactus, name='contactus-page'),
    path('login',views.login, name='login-page'),
    path('singup',views.singup,name='singup-page'),
    # path('rent',views.rent,name='rent-page'),
    path('cart',views.cart,name='cart-page'),
    # path('reg',views.reg,name='reg-page')
    # path('logout',views.logout,name='about-page')
    path('user-reg',views.userReg,name='userReg'),
    path('reg',views.reg,name='reg-page'),
    path('readmore',views.readmore,name='readmore-page'),

]