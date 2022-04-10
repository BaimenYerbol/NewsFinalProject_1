from django.forms import *
from .models import Post, Author, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['postAuthor', 'postCategory', 'nameCategory', 'head', 'text']