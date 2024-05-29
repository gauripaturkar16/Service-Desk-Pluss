from django.urls import path

from . import views

urlpatterns =[
    path('register_cust/', views.register_cust, name='register_cust' ),
    path('login/', views.login_user, name='login' ),
    
    path('logout/', views.logout_user, name='logout' )
    ]
