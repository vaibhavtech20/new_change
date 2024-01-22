from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required 
# from .models import kumbi
from .models import MatrimonialProfile
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import loader
from django.views.generic import  ListView
from django.template import loader
from django.urls import reverse
# from .forms import kumbiForm
# Create your views here.
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from acc.models import CustomUser

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Create a new user instance
        if password == password1:
            user = CustomUser(email=email,fullname=fullname)
            user.set_password(password)
            user.save()
            return redirect('login')
        # Optionally, log the user in after registration
        # login(request, user)
        else:
            messages.info(request, 'Passwords do not match.')
          # Redirect to the login page or another desired page

    return render(request, 'register.html')


def login(request):
    if request.session.has_key('is_logged'):
        return redirect('profile')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
       
        if user is not None:
            auth.login(request, user)
            request.session['is_logged'] = True
            return redirect('profile')
            # login(request, user)
            # messages.success(request, 'Login successful!')
            # return redirect('profile')
        else:
            messages.info(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')

def logout(request): 
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    MatrimonialProfiles= MatrimonialProfile.objects.all()
    data = {
          'MatrimonialProfiles' : MatrimonialProfiles,
    }
    # return render(request, 'home.html',data)
    return render(request,'profile.html',data)

# views.py

# @login_required(login_url='login')
# def profile(request):
#     # Assuming the user is logged in
#     if request.user.is_authenticated:
#         user_name = request.user.name 
#         user_profile = MatrimonialProfile.objects.get(user=request.name)
#         other_profiles = MatrimonialProfile.objects.exclude(user=request.name)
#         return render(request, 'profile.html', {'user_name': user_name,'user_profile': user_profile, 'other_profiles': other_profiles})
#         # return render(request, 'profile.html', {'user_profile': user_profile, 'other_profiles': other_profiles})
#     else:
#         # Handle the case where the user is not logged in
#         return render(request, 'profile.html', {'user_name': None,'user_profile': None, 'other_profiles': None})
#         # return render(request, 'profile.html', {'user_profile': None, 'other_profiles': None})



# def profile(request):

#     user = request.user
#     # Retrieve logged-in user's profile
#     user_profile = MatrimonialProfile.objects.get(user=user)

#     # Retrieve all other profiles (excluding the logged-in user)
#     all_profiles = MatrimonialProfile.objects.exclude(user=user)

#     context = {
#         'user_profile': user_profile,
#         'all_profiles': all_profiles,
#     }

#     return render(request, 'profiles.html', context)



def home(request):
    return render(request,'home.html')

# views.py

# from django.shortcuts import render, redirect
from .forms import MatrimonialProfileForm

def create_profile(request):
    if request.method == 'POST':
        form = MatrimonialProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a success page
    else:
        form = MatrimonialProfileForm()

    return render(request, 'create_profile.html', {'form': form})





