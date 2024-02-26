"""
URL configuration for sample_project2 project.

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
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view, name='login'),
    path('home/',home_view, name='home'),
    path('fhome/',fhome_view, name='faculty_home'),
    path('logout/',authlogout, name='logout'),
    path('create/',insert_data, name='insert'),
    path('',login_view)
]
