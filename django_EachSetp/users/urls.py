





from django.conf.urls import url
from django.urls import path,include
from users import views


from users.models import UserModel
from users.serializers import UserSerializers

#---------------------routers视图
from rest_framework import routers
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'v6/user', views.UserModelViews,basename='v6')
router.register(r'v7/user', views.CreateListRetrieveViewSet,basename='v7')
#-----------------------------------


urlpatterns = [
    path(r'v0/user',views.Users.as_view()),
    path(r'v1/user',views.Users.as_view()),
    path(r'v2/user',views.UserViews.as_view()),
    path(r'v3/user',views.UserViews.as_view(queryset=UserModel.objects.all(),serializer_class=UserSerializers),name='v3'),
    path(r'v4/user',views.PermissionView.as_view()),
    path(r'v5/user',views.example_view),


    #---------routers视图
    path(r'',include(router.urls)),

]





