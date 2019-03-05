from django import forms
from .models import Album

class AlbumPost(forms.Form):
    title = forms.CharField(max_length=50)
    artist = forms.CharField(max_length=50)
    cover = forms.ImageField()
    review = forms.CharField()
