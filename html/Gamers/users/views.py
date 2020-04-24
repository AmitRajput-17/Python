from django.shortcuts import render

from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User 


def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'success.html', {'form':form} )
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})  