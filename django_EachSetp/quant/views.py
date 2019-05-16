from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework.views import APIView,Response




class Quant(APIView):
    '''quant '''
    def get(self,request):
        return Response({'hello':'get'})

    def post(self,request,*args,**kwargs):
        return Response({'post':'post'})


class QuantForex(APIView):
    '''quant forex'''
    def get(self,request):
        return Response({'hello':'get'})

    def post(self,request,*args,**kwargs):
        return Response({'post':'post'})









