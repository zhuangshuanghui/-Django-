from django import forms
from app2005050209.models import Article,UserProfile,User
from django.forms import Textarea,fields

class ArticleForm(forms.ModelForm):
    """Form definition for Page."""

    class Meta:
        """Meta definition for Pageform."""

        model = Article
        fields ='__all__'
        widgets = {
            'content': Textarea(attrs={'cols': 90, 'rows': 20}),
        }

class UserForm(forms.ModelForm):
    	 # 输入密码不回显
	password = 	forms.CharField(widget=forms.PasswordInput(),label="密码")	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('occupation', 'birthday','education','iphon','sex')

class LoginForm(forms.Form):
     username = fields.CharField(
        widget=forms.TextInput(attrs={'class':'ipt'}),
        label='姓名',
        required=True,)
     password = fields.CharField(
        widget=forms.PasswordInput(attrs={'class':'ipt'}),
        label='密码',
        required=True,)