from django.conf.urls import url
from rest_framework import routers
from django.urls import path,include


from rest_framework.documentation import include_docs_urls,get_docs_view
from rest_framework_swagger.views import get_swagger_view


from users.views import Users
from quant.views import Quant
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    # ----------接口文档类型
    url(r'swagger-docs/',get_swagger_view(title='swagger-docs')),

    path(r'users/',include('users.urls')),
    path(r'quant/',include('quant.urls')),

]











