







from rest_framework import serializers

from users.models import UserModel

class UserSerializers(serializers.Serializer):
# class UserSerializers(serializers.HyperlinkedModelSerializer):
    '''
    1.写post,put 请求方式的填写字段
    2.word说明
        help_text 显示请求时的帮助信息
        required  是否是必填项
        error_messages  错误输入提示

    '''
    name = serializers.CharField(max_length=100)
    age = serializers.CharField(max_length=100,help_text='this help docment!')
    like = serializers.CharField(max_length=100,required=False,error_messages={'error':'plese input right value!'})
    price = serializers.CharField(max_length=100,error_messages={'error':'plese input right value!'})


    def create(self, validated_data):
        '''
        1.serializers对请求方法进行实际操作
        '''
        return UserModel.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.like = validated_data.get('like', instance.like)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


    class Meta:
        model = UserModel
        fields = '__all__'



