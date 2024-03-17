"""HelloWorld URL Configuration

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
from . import testApi
from . import logistics_objects_api

urlpatterns = [
  path('admin/', admin.site.urls),
  path('testApi/hello', testApi.hello),
  path('testApi/token', testApi.generateToken),
  path('logistics_objects/getByAwbNum/<awbNum>', logistics_objects_api.getByAwbNum),
  path('logistics_objects/getAwbList', logistics_objects_api.getAwbList),
  path('logistics_objects/getByAwbNumList', logistics_objects_api.getByAwbNumList),
  path('logistics_objects/sort', logistics_objects_api.sort)
]
