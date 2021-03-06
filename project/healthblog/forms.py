from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','tag','author','body')

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'username','id':'authore','type':'hidden'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','tag','body')

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }