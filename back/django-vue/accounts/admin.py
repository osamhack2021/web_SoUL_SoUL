from django.contrib import admin
from .models import Profile, Follow


class FollowInline(admin.TabularInline):
    model = Follow
    fk_name = 'from_user'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user', 'number']
    list_display_links = ['nickname', 'user', 'number']
    search_fields = ['nickname','number','user', 'number']
    inlines = [FollowInline,]
    
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'created_at']
    list_display_links = ['from_user', 'to_user', 'created_at']