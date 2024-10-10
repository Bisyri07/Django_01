from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request=request, template_name='posts/posts_list.html')