from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Album
from .forms import AlbumPost
# Create your views here.

def home(request):
    albums = Album.objects
    album_list = Album.objects.all()
    paginator = Paginator(album_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'albums' : albums, 'posts':posts})

def detail(request, album_id):
    album_detail = get_object_or_404(Album, pk = album_id)
    return render(request,'detail.html', {'album' : album_detail})


def new(request):
    return render(request, 'new.html')

def create(request):
    album = Album()
    album.title = request.GET['title']
    album.artist = request.GET['artist']
    album.review = request.GET['review']
    album.cover = 'images/' + request.GET['cover'] 
    album.release_date = timezone.datetime.now()
    album.save()
    return redirect('/album/' + str(album.id))

def albumpost(request):
    #입력된 내용 처리
    if request.method == 'POST':
        form = AlbumPost(request.POST)
        #제대로된 값이 입력됐는지 확인
        if form.is_valid():
            post = form.save(commit=False)
            post.release_date = timezone.datetime.now()
            post.save()
            return ("home.html",{"posts":posts},{"form":form})
    #빈페이지를띄워줌
    else:
        form = AlbumPost()
        return render(request, 'new.html', {'form':form})
