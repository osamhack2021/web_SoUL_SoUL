from django import forms
from .models import Post
# from .models import Comment

class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='', required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 30,
        'cols': 50,
        'placeholder': '2000자 까지 등록 가능합니다'
    }))
    content_type = forms.CharField(label='', required=True)
    
    class Meta:
        model = Post
        fields = ['photo', 'content']
        # fields = ['content']
    
    
# class CommentForm(forms.ModelForm):
#     content = forms.CharField(label='', widget=forms.TextInput(attrs={
#         'class': 'comment-form',
#         'size': '70px',
#         'placeholder': '댓글 달기...',
#         'maxlength': '40', }))
    
#     class Meta:
#         model = Comment
#         fields = ['content']
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        