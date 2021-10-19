from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from . import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    
    path('post/', include('post.urls', namespace='post')),
    # path('', lambda r: redirect('post:post_list'), name='root'),
    path('', lambda r: redirect('post/'), name='root'),
    
    # path('', views.HomeView.as_view(), name='home'),
    path('postapi/', include('post.urls', namespace='post_api')),
    path('accountsapi/', include('accounts.urls', namespace='accounts_api')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns