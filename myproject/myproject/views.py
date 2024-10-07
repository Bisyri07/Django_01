# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello World this works!')
    return render(request=request, template_name='home.html')

def about(request):
    # return HttpResponse('My about page is here!')
    return render(request, 'about.html')