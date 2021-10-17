from rest_framework import serializers # serializer import
from .models import Profile, Follow # 선언한 모델 import


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # 모델 설정
        fields = ('id', 'user', 'nickname', 'number', 'follow_set', 'picture', 'about', 'gender', )  # 필드 설정
        
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('from_user', 'to_user')