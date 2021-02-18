from django.shortcuts import render, redirect
from .forms import DonerRegister
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'finder/index.html')


def register(request):
    if request.method == 'POST':
        form = DonerRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome Your account have been registerd')
            return redirect('index')
    else:
        form = DonerRegister()
    context = {
        'form': form,
    }
    return render(request, 'finder/register.html', context)


@login_required
def profile(request):
    return render(request, 'finder/profile.html')
