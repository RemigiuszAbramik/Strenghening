from django.views import generic
from .models import Post
from .forms import AddPost


class IndexView(generic.ListView):
    model = Post
    template_name = 'forum/index.html'
    ordering = ['-start_date']


class DetailView(generic.DetailView):
    model = Post
    template_name = 'forum/detail.html'


class CreateView(generic.CreateView):
    model = Post
    form_class = AddPost
    template_name = 'forum/add.html'
