"""django_EachSetp URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin

from django.urls import include,path

from rest_framework.documentation import include_docs_urls,get_docs_view
from rest_framework_swagger.views import get_swagger_view



urlpatterns = [


    # ----------接口文档类型
    # url(r'^docs/',get_swagger_view(title='Pastebin API')),
    url(r'docss/',include_docs_urls(title='Api Docment', description='write something.')),  # 需要建立superuser才能使用这个界面
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),



    path('admin/', admin.site.urls),
    path(r'api/',include('api.urls')),
    path(r'users/',include('users.urls')),
    path(r'quant/',include('quant.urls')),


]










