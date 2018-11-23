from django import forms
from .models import Price

class PostForm(forms.ModelForm):
    # forms의 ModelForm 클래스를 상속받는다.
    class Meta:
        model = Price # GuessNumbers와 연결
        fields = ('name', 'summary', 'discount', )