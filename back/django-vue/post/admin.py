from django import forms
from django.contrib import admin
from .models import Post, Like, Bookmark, Tag, Category, Question, MunhakType, Show


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = '__all__'

class LikeInline(admin.TabularInline):
    model = Like
        
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'nickname', 'title', 'intro', 'content', 'category', 'question', 'munhak_type', 'show', 'created_at', 'updated_at']
    list_display_links = ['author', 'nickname', 'title', 'content', 'category', 'show']
    form = PostForm
    inlines = [LikeInline]
    
    def nickname(request, post):
        return post.author.profile.nickname
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Question,QuestionAdmin)

class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Show,ShowAdmin)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']
    
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
    

    









