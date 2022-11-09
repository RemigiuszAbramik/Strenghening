from django.views import generic
from .models import Post, Comment
from .forms import AddPost, AddComment


class IndexView(generic.ListView):
    model = Post
    template_name = 'forum/index.html'
    ordering = ['-start_date']


class DetailView(generic.DetailView):
    model = Post
    template_name = 'forum/detail.html'


class CreatePost(generic.CreateView):
    model = Post
    form_class = AddPost
    template_name = 'forum/add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class CreateComment(generic.CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'forum/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.post = self.kwargs['pk']
        return super().form_valid(form)