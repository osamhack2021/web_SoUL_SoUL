from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import re



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/post/category/{self.slug}/'
    
    class Meta:
        verbose_name_plural = 'Categories'
        
           
class Question(models.Model):
    name = models.CharField(max_length=50, unique=True)
    content = models.CharField(max_length = 100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/post/question/{self.slug}/'
    
    


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    intro = models.CharField(max_length=300, help_text="최대 300자 입력 가능", blank=True)
    content = models.CharField(max_length=3000, help_text="최대 3000자 입력 가능")
    category = models.ForeignKey(Category,
                                 null=True,
                                 on_delete=models.PROTECT)
    question = models.ForeignKey(Question,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT)
    is_no_public = models.BooleanField(default=False, verbose_name = '비공개')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like')  # post.like_set 으로 접근 가능
    bookmark_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='bookmark_user_set',
                                           through='Bookmark')  # post.like_set 으로 접근 가능

    # class Meta:
    #     ordering = ['-created_at']


    @property
    def like_count(self):
        return self.like_user_set.count()
    @property
    def bookmark_count(self):
        return self.bookmark_user_set.count()

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author} :: {self.category}'
    
    def get_absolute_url(self):
        return f'/post/{self.pk}/'
    
    def get_question(self):
        return self.question.content
    
    def get_public_option(self):
        return self.is_no_public.default

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://api.adorable.io/avatars/60/{self.author.username}.png'
    

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'post')
        )

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'post')
        )
        

    
    
    

        





