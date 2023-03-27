from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
        
    context = {'form':form}
    return render(request, 'account/registration/register.html', context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form':form}
    return render(request, 'account/my-login.html', context)

#Logout
def user_logout(request):
    auth.logout(request)
    return redirect('store')

@login_required(login_url='my-login') #The decorator prevents unauthenticated users from login in
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required(login_url='my-login') 
def profile_management(request):

    #updating username and email 

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')
        
    #To populate the user's information
    user_form = UpdateUserForm(instance=request.user)

    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context)

@login_required(login_url='my-login') 
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        return redirect('store')
    return render(request,'account/delete-account.html')
    