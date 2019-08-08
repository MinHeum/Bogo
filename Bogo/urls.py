"""Bogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
import parsed_data.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',parsed_data.views.home, name='home'),
    path('login/',parsed_data.views.login, name='login'),
    path('add/',parsed_data.views.addGoods, name = 'addGoods'),
    path('post/',parsed_data.views.post, name = 'post'),
    path('post/<int:post_id>',parsed_data.views.detail, name = 'post_detail'),
    path('post/new',parsed_data.views.new, name = 'post_new'),
    path('post/create',parsed_data.views.create, name='post_create'),
    path('accounts/',include('allauth.urls')),
]
