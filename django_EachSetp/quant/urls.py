
from django.conf.urls import url,include
from rest_framework import routers


from quant import views


urlpatterns = [

    url(r'quant',views.Quant.as_view()),
    url(r'quantForex',views.QuantForex.as_view()),

]






