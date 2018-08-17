#from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
  latest_posts = Post.objects.order_by('-pub_date')[:5]
  #template = loader.get_template('posts/index.html')
  context = {'latest_posts': latest_posts}
  # return HttpResponse(template.render(context, request))
  return render(request, 'posts/index.html', context)


def detail(request, post_id):
  try:
    post = Post.objects.get(post_id)
  except Post.DoesNotExist:
    raise Http404("Post does not exist")
  return render(request, 'posts/detail.html', {'post': post})
