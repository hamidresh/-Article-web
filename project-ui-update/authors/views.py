from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login , authenticate 
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Profile_authors
from .forms import BioForm , ProfileConfirmationForm

@login_required
def profiles(request):
    user_profile, created = Profile_authors.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        bio_form = BioForm(request.POST, instance=user_profile)
        if bio_form.is_valid():
            bio_form.save()
            return redirect('profiles')
    else:
        bio_form = BioForm(instance=user_profile)

    context = {'user_profile': user_profile, 'bio_form': bio_form}
    return render(request, 'profiles.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('essay_list')  # Redirect to the profiles page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def loginPage(request):    
    page = 'login'
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('essay_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login_register.html', {'form': form})

def confirmationauthors (request):
    profiles = Profile_authors.objects.filter(confirmation=False)

    forms = []

    if request.method == 'POST':
        for profile in profiles:
            form = ProfileConfirmationForm (request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('confirmation')
            
    else:
        for profile in profiles:
            forms.append(ProfileConfirmationForm (instance=profile))
    return render(request,'confirm_account.html',{'profiles': profiles, 'forms': forms})
       
        


