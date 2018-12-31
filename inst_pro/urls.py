"""inst_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import inst_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',inst_app.views.reg,name = 'reg'),
    path('',inst_app.views.Login),
    path('home',inst_app.views.home,name='home'),
    path('service',inst_app.views.services , name = 'services'),
    path('contact',inst_app.views.contact, name = 'contact'),
    path('feedback',inst_app.views.feedback, name='feedback'),
    path('gal',inst_app.views.gal,name= 'gal')

]
