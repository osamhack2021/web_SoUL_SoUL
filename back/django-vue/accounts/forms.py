from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
    
    
class SignupForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자, 공백 입력불가',
    }))
    
    nickname = forms.CharField(label='닉네임')
    picture = forms.ImageField(label='프로필 사진', required=False)
    number = forms.CharField(label='군번')
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
        
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('이미 존재하는 닉네임 입니다.')
        return nickname
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 사용중인 이메일 입니다.')
        return email
    
    def clean_number(self):
        number = self.cleaned_data.get('number')
        if Profile.objects.filter(number=number).exists():
            raise forms.ValidationError('이미 사용중인 군번입니다.')
        return number

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture:
            picture = None
        return picture
    
    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            nickname=self.cleaned_data['nickname'],
            number=self.cleaned_data['number'],
            picture=self.cleaned_data['picture'],
        )
        return user
    
class UpdateProfile(forms.ModelForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자, 공백 입력불가',
    }))
    nickname = forms.CharField(label='닉네임')
    picture = forms.ImageField(label='프로필 사진', required=False)
    number = forms.CharField(label='군번')
    email = forms.EmailField(required=True)
    about = forms.CharField(label='소개글')
    gender = forms.CharField(label='성별')

    class Meta:
        model = User
        fields = ('username', 'nickname', 'picture', 'number', 'email', 'about', 'gender')

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('이미 존재하는 닉네임 입니다.')
        return nickname
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 사용중인 이메일 입니다.')
        return email
    
    def clean_number(self):
        number = self.cleaned_data.get('number')
        if Profile.objects.filter(number=number).exists():
            raise forms.ValidationError('이미 사용중인 군번입니다.')
        return number

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture:
            picture = None
        return picture

    def save(self):
        user = super(SignupForm, self).save(coommit=False)
        user.username = self.cleaned_data['username']
        user.nickname = self.cleaned_data['nickname']
        user.email = self.cleaned_data['email']
        user.number = self.cleaned_data['number']
        user.picture = self.cleaned_data['picture']
        
        if commit:
            user.save()
        
        return user


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    