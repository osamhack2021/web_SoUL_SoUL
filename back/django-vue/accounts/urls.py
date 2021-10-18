from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers  # router import

app_name = 'accounts'
router = routers.DefaultRouter()  # DefaultRouter 설정
router.register('profile', views.ProfileViewSet)  # ViewSet과 함께 user라는 router 등록
router.register('follow', views.FollowViewSet)

urlpatterns = [
    
    path('', include(router.urls)), 
    
    path('signup/', signup, name='signup'),
    path('login/', login_check, name='login'),
    path('logout/', logout, name='logout'),
    path('follow/', follow, name='follow'),
    path('update_profile/', update_profile, name='update_profile')
    
]