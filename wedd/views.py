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
# from .forms import MatrimonialProfileForm , ProfilePictureForm
from .forms import MatrimonialProfileForm 

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Create a new user instance
        if password == password1:
            user = CustomUser(email=email,name=name)
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


# @login_required(login_url='login')
# def profile(request):
#     user = request.user
#     user_profile_exists = MatrimonialProfile.objects.filter(user=user).exists()

#     if user_profile_exists:
#         MatrimonialProfiles = MatrimonialProfile.objects.all()
#         data = {
#             'MatrimonialProfiles': MatrimonialProfiles,
#         }
#         return render(request, 'profile.html', data)
#     else:
#         return redirect('create_profile')

# @login_required(login_url='login')
# def profile(request):
#     user_profile_exists = MatrimonialProfile.objects.filter(email=request.user.email).exists()

#     if user_profile_exists:
#         MatrimonialProfiles = MatrimonialProfile.objects.all()
#         data = {
#             'MatrimonialProfiles': MatrimonialProfiles,
#         }
#         return render(request, 'profile.html',  data)
#     else:
#         return redirect('create_profile')

# @login_required(login_url='login')
# def profile(request):
#     # यहां हम request.user.profile का उपयोग करके उपयोगकर्ता की प्रोफ़ाइल की जानकारी प्राप्त कर रहे हैं।
#     user_profile = request.user.email

#     # प्रोफ़ाइल मौजूद है या नहीं यह जाँचें
#     if user_profile:
#         MatrimonialProfiles = MatrimonialProfile.objects.all()
#         data = {
#             'user_profile': user_profile,
#             'MatrimonialProfiles': MatrimonialProfiles,
#         }
#         return render(request, 'profile.html', data)
#     else:
#         # प्रोफ़ाइल नहीं है, तो प्रोफ़ाइल बनाने के लिए पेज पर पुनर्निर्देशित करें
#         return redirect('create_profile')

@login_required(login_url='login')
def profile(request):
    try:
        user_profile = MatrimonialProfile.objects.get(email=request.user.email)
    except MatrimonialProfile.DoesNotExist:
        # If the profile doesn't exist, redirect to the profile creation page or handle it as per your requirements
        return redirect('create_profile')

    other_profiles = MatrimonialProfile.objects.exclude(email=request.user.email)
    
    context = {
        'user_profile': user_profile,
        'other_profiles': other_profiles,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='login')
def create_profile(request):
    if request.method == 'POST':
        form = MatrimonialProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace 'profile_list' with the URL pattern for listing profiles
    else:
        form = MatrimonialProfileForm()
    
    return render(request, 'create_profile.html', {'form': form})

@login_required(login_url='login')
def update_profile(request):
    user_profile = MatrimonialProfile.objects.get(email=request.user.email)

    if request.method == 'POST':
        form = MatrimonialProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the user's profile page after successful update
    else:
        form = MatrimonialProfileForm(instance=user_profile)

    context = {
        'form': form,
    }

    return render(request, 'update_profile.html', context)



# def create_profile(request):
#     if request.method == 'POST':
#         profile_form = MatrimonialProfileForm(request.POST)
#         # picture_form = ProfilePictureForm(request.POST, request.FILES)
#         #  and picture_form.is_valid()
#         if profile_form.is_valid():
#             profile = profile_form.save(commit=False)
#             profile.user = request.user
#             profile.save()

#             # picture = picture_form.save(commit=False)
#             # picture.save()
            
#             # profile.profile_pics.add(picture)

#             return redirect('profile')  # Redirect to the profile page or any other page
#     else:
#         profile_form = MatrimonialProfileForm()
#         # picture_form = ProfilePictureForm()

#     return render(request, 'create_profile.html', {'profile_form': profile_form})
#     # , 'picture_form': picture_form
        
# def create_profile(request):
#     if request.method == 'POST':
#         form = MatrimonialProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')  # Redirect to a success page
#     else:
#         form = MatrimonialProfileForm()

#     return render(request, 'create_profile.html', {'form': form})


# @login_required(login_url='login')
# def profile(request):
#     MatrimonialProfiles= MatrimonialProfile.objects.all()
#     data = {
#           'MatrimonialProfiles' : MatrimonialProfiles,
#     }
#     # return render(request, 'home.html',data)
#     return render(request,'profile.html',data)

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
# from .forms import MatrimonialProfileForm

# def create_profile(request):
#     if request.method == 'POST':
#         form = MatrimonialProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to a success page
#     else:
#         form = MatrimonialProfileForm()

#     return render(request, 'create_profile.html', {'form': form})





