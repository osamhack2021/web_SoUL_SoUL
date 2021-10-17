from django import forms
from django.contrib import admin
from .models import Post, Like, Bookmark, Category, Question, MunhakType


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = '__all__'

class LikeInline(admin.TabularInline):
    model = Like
        
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'nickname', 'title', 'intro', 'content', 'category', 'question', 'munhak_type', 'is_no_public']
    list_display_links = ['author', 'nickname', 'title', 'content', 'category', 'is_no_public']
    form = PostForm
    inlines = [LikeInline]
    
    def nickname(request, post):
        return post.author.profile.nickname

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']
    
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# class TagAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
    
class MunhakTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

    
admin.site.register(Category,CategoryAdmin)    
admin.site.register(Question,QuestionAdmin)
# admin.site.register(Tag, TagAdmin)
admin.site.register(MunhakType, MunhakTypeAdmin)
    
    
    

    









