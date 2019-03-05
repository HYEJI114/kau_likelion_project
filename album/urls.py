from django.urls import path
from . import views
    
urlpatterns = [
    path('<int:album_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    #path('new/', views.albumpost, name='new'),
]