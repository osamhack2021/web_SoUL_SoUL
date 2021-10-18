from rest_framework import serializers # serializer import
from .models import Category, Question, Post, Like, Bookmark # 선언한 모델 import

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 모델 설정
        fields = ('id', 'name', 'slug')  # 필드 설정
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'content', 'slug')
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'intro', 'content', 'category', 'question',  'is_no_public', 'created_at', 'updated_at', 'like_user_set', 'bookmark_user_set')
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at', 'updated_at')
        
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'post', 'created_at', 'updated_at')