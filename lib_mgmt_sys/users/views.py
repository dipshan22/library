from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def register(request):
    if request.method == 'GET':
        form = CreateUserForm()
        print(form)
        return render(request, 'register.html', {"forms":form})

    else:
        form = CreateUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html', {"forms":form})

