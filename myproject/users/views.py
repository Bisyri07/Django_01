from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   # create post form
        if form.is_valid():
            form.save()         
            return redirect("posts:list")
    else:
        form = UserCreationForm() 
        
    return render(
        request=request,
        template_name='users/register.html',
        context={'form':form}
    )

