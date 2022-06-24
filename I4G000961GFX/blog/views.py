
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):

    # specify the model for list  view
    model = Post

class PostCreateView(ListView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "_all_"
    success_url  = reverse_lazy("blog:all")
