"""
URL configuration for pro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import index,about,order,recipes,Home,dietplan,a,b,order2,order3,order4,order5,order6,order7,order8,c,d,e,f,g,h,bd,bc,be,bf,bg,register,doregister,viewusers,modify,login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index),
    path("about/",about),
    path("order/",order),
    path("recipes/",recipes),
    path("register/",register),
    path("Home/",Home),
    path("dietplan/",dietplan),
    path("a/",a),
    path("b/",b),
    path("c/",c),
    path("d/",d),
    path("e/",e),
    path("f/",f),
    path("g/",g),
    path("h/",h),
    path("order2/",order2),
    path("order3/",order3),
    path("order4/",order4),
    path("order5/",order5),
    path("order6/",order5),
    path("order7/",order7),
    path("order8/",order8),
    path("bc/",bc),
    path("bd/",bd),
    path("be/",be),
    path("bf/",bf),
    path("bg/",bg),
    path('doregister/', doregister),
   
    path('login/', login),
    path('viewusers/', viewusers),
    path('modify/', modify),

    
    
    
]
