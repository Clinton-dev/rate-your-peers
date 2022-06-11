from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def registration(request):
    context = {
        'title': 'signup',
        'form': ''
    }

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully, you can now login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        context['form'] = form

    return render(request, 'users/register.html', context)

@login_required
def settings(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Profile updated successfully!')
            return redirect('settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/settings.html', context)