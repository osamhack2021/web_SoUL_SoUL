from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='', required=True)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 30,
        'cols': 50,
        'placeholder': '2000자 까지 등록 가능합니다'
    }))
    category = forms.CharField(label='', required=True)
    question = forms.CharField(label='', required=True)
    show = forms.CharField(label='', required=True)
    
    class Meta:
        model = Post
        fields = ['content', 'title', 'category', 'question', 'show']

    
    

        
        

        
        
        
        
        
        
        