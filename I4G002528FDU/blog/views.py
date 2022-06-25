from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.views.generic.edit import CreateView, UpdateView, BaseDetailView
from django.views.generic import ListView, DetailView

# Create your views here.


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')


class PostDeleteView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')