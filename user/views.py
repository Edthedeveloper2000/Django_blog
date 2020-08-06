from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        print("test 1")
        if form.is_valid():
            print("vai dar errado aqui :(")
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
    if request.method == 'POST':
        # user = User.objects.all().filter(username='EdGames').first()
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request,f'your account has been updated')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'user/profile.html', context)
    