from django.views import generic
from .models import Training

class IndexView(generic.ListView):
    template_name = 'training/index.html'

    def get_queryset(self):
        return Training.objects.all()


class DetailView(generic.DetailView):
    model = Training
    template_name = 'training/base.html'
