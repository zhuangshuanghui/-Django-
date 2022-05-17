"""zhuangshuanghui2005050209 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app2005050209 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('addbook/',views.addbook,name='addbook'),                      #添加
    path('editbooks/<int:id>/',views.editbooks,name='editbooks'),       #编辑
    path('lookbooks/',views.lookbooks,name='lookbooks'),                #主页面
    path('deletebooks/<int:id>',views.deletebooks,name='deletebooks'),  #删除
    path('onebooks/<int:id>',views.onebooks,name='onebooks'),           #显示
    path('fenleibooks/<int:id>',views.fenleibooks,name='fenleibooks'),  #分类显示
    path('allbooks/<int:pagenum>/',views.allbooks,name='allbooks'),     #显示全部文章
    path("register/",views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    #path('deny/',views.deny,name="deny"),
    path("readsession",views.readSession,name="readsession"),

]
