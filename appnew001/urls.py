from django.urls import path
from . import views

urlpatterns = [
    path('', views.hanan, name="hanan"),
    path('func', views.newfunc,name="newfunc"),
    path('newfunc01',views.newfunc01,name="newfunc01"),
    path('login',views.loginfun,name="loginfun"),
    path('index',views.indexfun,name='indexfun'),
    path('404',views.error,name='error'),
    path('about',views.about,name='about'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('news',views.news,name='news'),
    path('shop',views.shop,name='shop'),
    path('signup',views.signup,name='signup'),
    path('singlen',views.singlen,name='singlen'),
    path('singlep',views.singlep,name='singlep')
    

]