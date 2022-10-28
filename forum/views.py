from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    model = Post
    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    model = Post
    template_name = 'forum/base.html'
