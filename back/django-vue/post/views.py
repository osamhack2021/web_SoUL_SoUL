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
from .models import Post, Like, Bookmark, Category, Question

from rest_framework import viewsets # vieset import
from .serializers import CategorySerializer, QuestionSerializer, PostSerializer, LikeSerializer, BookmarkSerializer # 생성한 serializer import
from .models import Category, Question, Post, Like, Bookmark # 선언한 모델 import



class CategoryViewSet(viewsets.ModelViewSet): # ModelViewSet 활용
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['public'] = Post.objects.filter(is_no_public=False)
        return context
    
class FootprintList(ListView):
    model = Question
    ordering = '-pk'
    paginate_by = None
    
    def get_context_data(self, **kwargs):
        context = super(FootprintList, self).get_context_data()
        context['number'] = name.objects.all()
        context['questions'] = content.objects.all()
        return context
    
class PostDetail(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
    


    
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'intro', 'content', 'question', 'is_no_public']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            return response

        else:
                return redirect('/')
            
            
class SonagiCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'is_no_public']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(SonagiCreate, self).form_valid(form)

            return response

        else:
                return redirect('/sonagi/')
            
class FootprintCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['questions', 'content', 'is_no_public']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(FootprintCreate, self).form_valid(form)

            return response

        else:
                return redirect('/footprint/')
            
class BookCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'intro', 'content', 'is_no_public']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(BookCreate, self).form_valid(form)

            return response

        else:
                return redirect('/book/')
            
class MunhakCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'is_no_public']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(MunhakCreate, self).form_valid(form)

            return response

        else:
                return redirect('/munhak/')
    
    
    
    

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'intro', 'content', 'is_no_public']

    template_name = 'post/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)

        return response

    
class SonagiUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'is_no_public']

    template_name = 'post/sonagi_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(SonagiUpdate, self).get_context_data()

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(SonagiUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(SonagiUpdate, self).form_valid(form)
        return response
    
class FootprintUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['content', 'is_no_public']

    template_name = 'post/footprint_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(FootprintUpdate, self).get_context_data()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(FootprintUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(FootprintUpdate, self).form_valid(form)
        return response
    
class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'intro', 'content', 'is_no_public']

    template_name = 'post/book_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(BookUpdate, self).get_context_data()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(BookUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(BookUpdate, self).form_valid(form)
        return response
    
class MunhakUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'is_no_public']

    template_name = 'post/munhak_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(MunhakUpdate, self).get_context_data()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(MunhakUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(MunhakUpdate, self).form_valid(form)
        return response
    

    

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) 
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
    
class SonagiSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) & category.name=='Sonagi'
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(SonagiSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
    
class FootprintSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) & category.name=='Footprint'
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(FootprintSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
    
class BookSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) & category.name=='Book'
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(BookSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
    
class MunhakSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) & category.name=='Munhak'
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(MunhakSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
    
    
    
    
@login_required
def post_edit(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.warning(request, '잘못된 접근입니다')
        return redirect('post:post_list')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '수정완료')
            return redirect('post:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {
        'post': post,
        'form': form,
    })

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category)

    return render(
        request,
        'post/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'category': category,
        }
    )
    
@login_required
@require_POST
def post_bookmark(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_bookmark, post_bookmark_created = post.bookmark_set.get_or_create(user=request.user)

    if not post_bookmark_created:
        post_bookmark.delete()
        message = "북마크 취소"
    else:
        message = "북마크"

    context = {'bookmark_count': post.bookmark_count,
               'message': message}

    return HttpResponse(json.dumps(context), content_type="application/json") 


@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message}

    return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
@require_POST
def post_bookmark(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_bookmark, post_bookmark_created = post.bookmark_set.get_or_create(user=request.user)

    if not post_bookmark_created:
        post_bookmark.delete()
        message = "북마크 취소"
    else:
        message = "북마크"

    context = {'bookmark_count': post.bookmark_count,
               'message': message}

    return HttpResponse(json.dumps(context), content_type="application/json")    


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        # return redirect('post:post_list')
        return redirect('')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '삭제완료')
        # return redirect('post:post_list')
        return redirect('')
    
    
    
# @login_required
# def my_post_list(request, username):
#     user = get_object_or_404(get_user_model(), username=username)
#     user_profile = user.profile
#     target_user = get_user_model().objects.filter(id=user.id).select_related('profile') \
#         .prefetch_related('profile__follower_user__from_user', 'profile__follow_user__to_user')
#     post_list = user.post_set.all()
#     all_post_list = Post.objects.all()
#     category = Category.objects.get(slug=slug)
    
#     return render(request, 'post/my_post_list.html', {
#         'user_profile': user_profile,
#         'target_user': target_user,
#         'post_list': post_list,
#         'all_post_list': all_post_list,
#         'username': username,
#         'categories': Category.objects.all(),
#         'category': category,
#     })



@login_required
def my_post_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_profile = user.profile
    target_user = get_user_model().objects.filter(id=user.id).select_related('profile') \
        .prefetch_related('profile__follower_user__from_user', 'profile__follow_user__to_user')
    post_list = Post.objects.filter(category=category)
    category = Category.objects.get(slug=slug)
    
    return render(request, 'post/my_post_list.html', {
        'user_profile': user_profile,
        'target_user': target_user,
        'post_list': post_list,
        'all_post_list': all_post_list,
        'username': username,
        'categories': Category.objects.all(),
        'category': category,
    })

@login_required
def my_sonagi_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_profile = user.profile

    my_sonagi_list = user.post_set.filter(category='Sonagi')
    all_post_list = Post.objects.all()
    
    return render(request, 'post/my_sonagi_list.html', {
        'my_sonagi_list': my_sonagi_list,
    })

@login_required
def my_footprint_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_profile = user.profile

    my_footprint_list = user.post_set.filter(category='Footprint')
    all_post_list = Post.objects.all()
    
    return render(request, 'post/my_sonagi_list.html', {
        'my_footprint_list': my_footprint_list,
    })

@login_required
def my_book_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_profile = user.profile

    my_book_list = user.post_set.filter(category='Book')
    all_post_list = Post.objects.all()
    
    return render(request, 'post/my_sonagi_list.html', {
        'my_book_list': my_book_list,
    })

@login_required
def my_munhak_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_profile = user.profile

    my_book_list = user.post_set.filter(category='Munhak')
    all_post_list = Post.objects.all()
    
    return render(request, 'post/my_sonagi_list.html', {
        'my_munhak_list': my_munhak_list,
    })

    
    
    
    
    





    
    
    
    
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    
#     return render(request, 'post/post_detail.html', {
#         'post': post,
#     })

# def post_list(request):
#     post_list = Post.objects.all() \
#             .prefetch_related('like_user_set__profile', 'author__profile__follower_user', 'author__profile__follower_user__from_user') \
#             .select_related('author__profile')

#     paginator = None
        
#     if request.is_ajax():
#         return render(request, 'post/post_list_ajax.html', {
#             'posts': posts,
#         })

#     if request.user.is_authenticated:
#         username = request.user
#         user = get_object_or_404(get_user_model(), username=username)
#         user_profile = user.profile
#         follow_set = request.user.profile.get_following
#         follow_post_list = Post.objects.filter(author__profile__in=follow_set)
        
#         return render(request, 'post/post_list.html', {
#             'user_profile': user_profile,
#             'posts': posts,
#             'follow_post_list': follow_post_list,
#         })
#     else:
#         return render(request, 'post/post_list.html', {
#             'posts': posts,
#         })
    

# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.info(request, '새 글이 등록되었습니다')
#             return redirect('post:post_list')
#     else:
#         form = PostForm()
#     return render(request, 'post/post_new.html', {
#         'form': form,
#     })

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if post.author != request.user:
#         messages.warning(request, '잘못된 접근입니다')
#         return redirect('post:post_list')
    
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, '수정완료')
#             return redirect('post:post_list')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'post/post_edit.html', {
#         'post': post,
#         'form': form,
#     })

    










