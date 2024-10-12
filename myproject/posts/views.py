from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') # descending
    return render(request=request, 
                  template_name='posts/posts_list.html',
                  context={'posts':posts})

def post_page(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request=request, 
                  template_name='posts/post_page.html',
                  context={'post':post})
