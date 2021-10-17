from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='', required=True)
    intro = forms.CharField(label='', required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 30,
        'cols': 50,
        'placeholder': '3000자 까지 등록 가능합니다'
    }))
    is_no_public = forms.BooleanField(label='', required=True)
    
    class Meta:
        model = Post
        fields = ['content', 'title', 'is_no_public']


       
