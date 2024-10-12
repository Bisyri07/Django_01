from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') # descending
    return render(request=request, 
                  template_name='posts/posts_list.html',
                  context={'posts':posts})
