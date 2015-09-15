from django.shortcuts import render
from django.http import HttpResponse
from article.models import Post
from datetime import datetime

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, my_args):
	post = Post.objects.all()[int(my_args)]
	s = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
	return HttpResponse(s)

