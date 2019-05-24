from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,UpdateView
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy

#def homePageView(request):
#	return HttpResponse('Hello, World!')

# Create your views here.

class HomePageView(ListView):
	model=Post
	template_name = 'blog/home.html'

class BlogListView(ListView):
	model=Post
	template_name='blog/home.html'

class BlogDetailView(DetailView):
	model=Post
	template_name='blog/post_detail.html'

class AboutPageView(TemplateView):
	template_name = 'blog/about.html'


class BlogCreateView(CreateView):
	model=Post
	template_name='blog/post_new.html'
	fields = '__all__'
	#success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
	model = Post
	fields = ['title', 'body']
	template_name = 'blog/post_edit.html'
	success_url = reverse_lazy('home')