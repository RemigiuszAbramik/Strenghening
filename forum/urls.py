from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.CreatePost.as_view(), name='add'),
    path('<int:pk>/addcomment/', views.CreateComment.as_view(), name='addc'),
]
