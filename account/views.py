from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

    #To loop through all the session keys:
    try:
        for key in list(request.session.keys()):
            if key == 'session_key':
                continue
            else:
                del request.session[key]

    except KeyError:
        pass
    messages.success(request, "logout success")

    return redirect('store')

@login_required(login_url='my-login') #The decorator prevents unauthenticated users from login in
def dashboard(request):
    return render(request, 'account/dashboard.html')

# Update
@login_required(login_url='my-login') 
def profile_management(request):

    #updating username and email 
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.info(request, "Account updated") #'info' so that does not get confused with the other 2 messages from delete(line 83) and logout(line 49)
            return redirect('dashboard')
        
    #To populate the user's information

    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context)

# Delete
@login_required(login_url='my-login') 
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        messages.error(request, "Account deleted") #It's send to 'error' instead of 'success' to avoid two messages stemming from base.html line 177
        return redirect('store')
    return render(request,'account/delete-account.html')
    