from django.shortcuts import render, redirect
from .forms import DonerRegister
from django.contrib import messages


def home(request):
    return render(request, 'finder/index.html')


def register(request):
    form = DonerRegister()
    if request.method == 'POST':
        form = DonerRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome Your account have been registerd')
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'finder/register.html', context)
