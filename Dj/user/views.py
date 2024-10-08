from django.shortcuts import render, redirect
from django.contrib import auth, messages

from user.models import User, Profile
from user.forms import RegisterUser


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning()
        # TODO : 
        return redirect('')
    if request.method == "POST":

        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, phone=phone, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'خوش آمدید')
            # TODO : 
            return redirect('')
        else:
            messages.error(request, 'مشخصات وارد شده اشتباه می باشد، دوباره تلاش کنید')
            return render(request, 'user/login.html')
    return render(request, "user/login.html")


def logoutUser(request):
    auth.logout(request)
    messages.info()
    # TODO : 
    return redirect("")


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning()
        # TODO : 
        return redirect('')
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(email=email, username=username, password=password,first_name=first_name,
                                            last_name=last_name, phone=phone)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'اطلاعات شما با موفقیت ثبت گردید')
            # TODO : 
            return redirect('')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('')
    else:
        form = RegisterUser()
    return render(request, "user/register.html", {'form': form})


def userProfile(request):
    if request.user.is_authenticated:
        p = Profile.objects.get(user=request.user)
        return render(request, "user/profile.html", {'profile':p})
    else:
        messages.warning(request, "وارد شوید")
        return redirect("")
