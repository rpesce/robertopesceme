from django.urls import path

from . import views

urlpatterns = [
    path('livros', views.PostListView, name='home'),
    path('new', views.NewPostListView, name='new_home'),
    path('past', views.PastPostListView, name='past_home'),
]