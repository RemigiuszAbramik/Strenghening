from django.views import generic
from .models import Post
from .forms import AddPost, AddComment
from django.views.generic.edit import FormMixin
from django.urls import reverse


class IndexView(generic.ListView):
    model = Post
    template_name = 'forum/index.html'
    ordering = ['-start_date']


class DetailView(FormMixin ,generic.DetailView):
    model = Post
    template_name = 'forum/detail.html'
    form_class = AddComment
    
    def get_success_url(self):
        return reverse('forum:detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = AddComment(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.save()
        return super(DetailView, self).form_valid(form)


class CreatePost(generic.CreateView):
    model = Post
    form_class = AddPost
    template_name = 'forum/add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
