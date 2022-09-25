from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.


class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-publish')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model =  Post
    template_name = 'post_detail.html'
