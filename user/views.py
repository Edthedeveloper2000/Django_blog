from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        print("test 1")
        if form.is_valid():
            form.save()
            print("test 2")
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account has been created, now you\'re able to log in ')
            return redirect('login')
    else:   
        form = UserRegistration()
    return render(request,'user/register.html',{'form': form})

@login_required
def profile(request):
   # user = User.objects.all().filter(username='EdGames').first()
    return render(request,'user/profile.html')
    