from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control mt-3'})
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control my-3'})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control mt-2'})
        }
