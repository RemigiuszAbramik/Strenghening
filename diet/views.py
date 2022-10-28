from django.views import generic
from .models import Diet

class IndexView(generic.ListView):
    template_name = 'diet/index.html'
    model = Diet
    def get_queryset(self):
        return Diet.objects.all()


class DetailView(generic.DetailView):
    model = Diet
    template_name = 'diet/base.html'
