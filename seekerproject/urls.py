"""seekerproject URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from seekerapp.models import *
from seekerapp.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'companies', Companies, 'company')
router.register(r'employees', Employees, 'employee')
router.register(r'interviews', Interviews, 'interview')
router.register(r'seekers', Seekers, 'seeker')
router.register(r'users', Users, 'user')
router.register(r'interviewTypes', InterviewTypes, 'interviewType')
router.register(r'applications', Applications, 'application')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', register_user), 
    path('login', login_user)
]
