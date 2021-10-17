from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers  # router import

app_name = 'post'
router = routers.DefaultRouter()  # DefaultRouter 설정
router.register('category', views.CategoryViewSet)  # ViewSet과 함께 user라는 router 등록
router.register('question', views.QuestionViewSet)
router.register('munhak_type', views.MunhakTypeViewSet)
router.register('post', views.PostViewSet)
router.register('like', views.LikeViewSet)
router.register('bookmark', views.BookmarkViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    
    path('list/', views.PostList.as_view()),
    path('footprint_list/', views.FootprintList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    
    path('create_post/', views.PostCreate.as_view()),
    path('create_sonagi/', views.SonagiCreate.as_view()),
    path('create_footprint/', views.FootprintCreate.as_view()),
    path('create_book/', views.BookCreate.as_view()),
    path('create_munhak/', views.MunhakCreate.as_view()),
    
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('update_sonagi/<int:pk>/', views.SonagiUpdate.as_view()),
    path('update_footprint/<int:pk>/', views.FootprintUpdate.as_view()),
    path('update_book/<int:pk>/', views.BookUpdate.as_view()),
    path('update_munhak/<int:pk>/', views.MunhakUpdate.as_view()),
    
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('sonagisearch/<str:q>/', views.SonagiSearch.as_view()),
    path('footprintsearch/<str:q>/', views.FootprintSearch.as_view()),
    path('booksearch/<str:q>/', views.BookSearch.as_view()),
    path('munhaksearch/<str:q>/', views.MunhakSearch.as_view()),
    
    path('edit/<int:pk>/', post_edit, name='post_edit'),
    path('category/<str:slug>/', views.category_page),
    path('bookmark', post_bookmark, name='post_bookmark'),
    
    path('delete/<int:pk>/', post_delete, name='post_delete'),
    path('like', post_like, name='post_like'),
    
    path('<username>/list/', my_post_list, name='my_post_list'),
    # path('<username>/list/sonagi', my_sonagi_list, name='my_sonagi_list'),
    # path('<username>/list/footprint', my_footprint_list, name='my_footprint_list'),
    # path('<username>/list/book', my_book_list, name='my_book_list'),
    # path('<username>/list/munhak', my_munhak_list, name='my_munhak_list'),
    
    
    
  
]