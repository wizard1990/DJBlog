from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from article.models import Post
from datetime import datetime
from django.http import Http404

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
	try:
		post = Post.objects.get(id=id)
	except Post.DoesNotExist:
		raise Http404
	return render(request, 'post.html', {'post': post})

def archives(request):
	try:
		post_list = Post.objects.all()
	except Post.DoesNotExist:
		raise Http404
	return render(request, 'archives.html', {'post_list':post_list, 'error': False})

def about_me(request):
	return render(request, 'aboutme.html')

def search_category(request, category):
  try:
    post_list = Post.objects.filter(category__cate_name__exact = category) #contains
  except Post.DoesNotExist:
    raise Http404
  return render(request, 'archives.html', {'post_list' : post_list})

def blog_search(request):
    if 'keyword' in request.GET:
      keyword = request.GET['keyword']
      if not keyword:
        return render(request,'home.html')
      else:
        post_list = Post.objects.filter(title__icontains = keyword)
        if len(post_list) == 0 :
          return render(request,'archives.html', {'post_list' : post_list, 'error' : True})
        else :
          return render(request,'archives.html', {'post_list' : post_list, 'error' : False})
    return redirect('/')