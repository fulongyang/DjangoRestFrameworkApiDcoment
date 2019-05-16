from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView,Response

from rest_framework import viewsets
from rest_framework import generics
from users.models import UserModel
from users.serializers import UserSerializers
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def example_view(request, format=None):
    '''需要提供IsAuthenticated 认证'''
    content = {
        'status': 'request was permitted'
    }
    return Response(content)


#----------------权限
class PermissionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)



# -------------mixin创建，删除
class UserViewMixin(object):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers


class UserModelViews(UserViewMixin,viewsets.ModelViewSet):
    
    pass



class CreateListRetrieveViewSet(UserViewMixin,mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    继承于mixin类 `UserViewMixin`.\n
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass



class UserViews(UserViewMixin,generics.ListCreateAPIView):
    '''
    1.创建用户\n
    2.获取用户详情\n
    3.views继承是限制允许使用的请求方式，具体要在serializer中建立方法的使用实例

    '''
    pass



#-------------测试
class Users(APIView):
    '''测试方法'''

    def get(self,request):
        '''用户详情\n1.information'''
        return Response({'get':'get'})

    def post(self,request,*args,**kwargs):
        '''注册用户\n1.wargs'''
        return Response({'post':'post'})

    def delete(self,request,*args,**kwargs):
        '''删除用户\n1.information'''
        return Response({'delete':'delete'})

    def put(self,request,*args,**kwargs):
        '''修改用户\n1.information'''
        return Response({'delete':'delete'})






