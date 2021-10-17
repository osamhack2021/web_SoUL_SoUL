from django.test import TestCase
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import re
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.utils.text import slugify
from django.db.models import Count
from .forms import PostForm
from .models import Post, Like, Tag, Bookmark, Category, Question


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    intro = models.CharField(max_length=300, help_text="최대 300자 입력 가능", blank=True)
    # content = MarkdownxField()
    content = models.CharField(max_length=3000, help_text="최대 3000자 입력 가능")
    category = models.ForeignKey(Category,
                                 null=True,
                                 on_delete=models.PROTECT)
    question = models.ForeignKey(Question,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT)
    munhak_type = models.ForeignKey(MunhakType,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT)
    # is_public = models.ForeignKey(Is_Public,
    #                          null=True,
    #                          on_delete=models.PROTECT)
    is_no_public = models.BooleanField(default=False, verbose_name = '비공개')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
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

    # # NOTE: content에서 tags를 추출하여, Tag 객체 가져오기, 신규 태그는 Tag instance 생성, 본인의 tag_set에 등록,
    # def tag_save(self):
    #     tags = re.findall(r'#(\w+)\b', self.content)

    #     if not tags:
    #         return

    #     for t in tags:
    #         tag, tag_created = Tag.objects.get_or_create(name=t)
    #         self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가

    @property
    def like_count(self):
        return self.like_user_set.count()
    @property
    def bookmark_count(self):
        return self.bookmark_user_set.count()

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    # def get_content_markdown(self):
    #     return markdown(self.content)
    
    def get_question(self):
        return self.question.content
    
    def get_public_option(self):
        return self.is_no_public.default

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://api.adorable.io/avatars/60/{self.author.username}.png'


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['public'] = Post.objects.filter(is_no_public=False)
        return context