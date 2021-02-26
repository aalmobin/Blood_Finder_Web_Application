from django.shortcuts import render, redirect
from .forms import DonerRegister, ProfileUpdate
from django.contrib import messages
from .models import Profile
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


@login_required
def updateprofile(request):
    if request.method == 'POST':
        p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile have been updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdate(instance=request.user.profile)
    context = {
        'p_form': p_form,
    }
    return render(request, 'finder/update_profile.html', context)


def search(request):
    if request.method == 'POST':
        group = request.POST['group']
        results = Profile.objects.filter(blood_group__icontains=group)
        context = {
            'results': results
        }
        return render(request, 'finder/search_blood.html', context)
    return render(request, 'finder/search_blood.html')


def donerInfo(request, pk):
    doner = Profile.objects.get(id=pk)

    context = {
        'doner': doner
    }
    return render(request, 'finder/doner.html', context)
