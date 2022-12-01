"""maxsop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views

from core.views import Index, About
from account.views import Signup

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('lead/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', About.as_view(), name='about'),
    path('sign-up/', Signup.as_view(), name='signup'),
    path('sign-in/', views.LoginView.as_view(template_name='account/signin.html'), name='signin'),
    path('sign-out/', views.LogoutView.as_view(), name='signout'),
    path('admin/', admin.site.urls),
]
