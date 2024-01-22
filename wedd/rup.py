# def register(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         fullname = request.POST.get('fullname')
#         password = request.POST.get('password')
#         password2= request.POST.get('confirm_password')

#         if password == password2:
#             # user = CustomUser.objects.create_user(email=email, fullname=fullname, password=password)
#             superuser = CustomUser.objects.create_superuser(email=email,fullname=fullname, password=password)
#             # login(request, user)
#             # messages.success(request, 'Registration successful!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match.')
#     return render(request, 'register.html')


# def register(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if pass1!=pass2:
#             messages.error(request, 'Your Password and Confirm Password Not Same..!')
#             # return HttpResponse("Your Password and Confirm Password Not Same..!")
#         else:
#             my_user=User.objects.create_user(username,email,pass1)
#             my_user.save()
#             return redirect('login')
#     return render(request,'register.html')

# def login(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         # email=request.POST.get('email')
#         pass1=request.POST.get('password')
#         # print(username,pass1)
#         User=authenticate(request,username=username,password=pass1)
#         if User is not None:
#             # login(request,User)
#             return redirect('profile')
#         else:
#             messages.info(request, 'invalid email or password')

#     return render(request,'login.html')

# def register(request):
#     if request.method == 'POST':
#         form = kumbiForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to a success page
#     else:
#         form = kumbiForm()

#     return render(request, 'register.html', {'form': form})


# def register(request):
#     return render(request,'register.html')

# def login(request):
#     return render(request,'login.html')

# def login(request):
#     if request.session.has_key('is_logged'):
#         return redirect('profile')
#     if request.method == 'POST/GET':
#         email = request.GET['email']
#         password = request.GET['password']
#         user=auth.authenticate(email=email,password=password)


#         if user is not None:

#             auth.login(request, user)
#             request.session['is_logged'] = True
#             return redirect('profile')
#         else:
#             messages.info(request, 'invalid email or password')
#             return redirect('login')

#     else:
#         return render(request, 'login.html')



# @login_required(login_url='login')
# def profile(request):
#     return render(request, 'profile.html')
# views.py

# from django.shortcuts import render
# from .utils import send_verification_email, generate_verification_code

# def register(request):
#     submitted = False
#     if request.method == "POST":
#         form = kumbiForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user to the database
#             messages.success(request,'User Register')
#             return HttpResponseRedirect('./regiter?submitted=True')
#     else:
#         form = kumbiForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'register.html', {'form': form,'submitted':submitted})
    #     # Send verification email to the user

    #     user_email = request.GET['email']  # User's email address
    #     verification_code = generate_verification_code()
    #     send_verification_email(user_email, verification_code)
    #     # Rest of the signup process
    #     # ...

    # return render(request, 'register.html')

# def profile(request):
#     user = request.user

#     context = {
#         "user": user,
#     }

#     return render(request, "profile.html", context)

# views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from .forms import LoginForm

# def login(request):
#     if request.method == 'POST':
#         form = kumbiForm(request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = auth.authenticate(request, email=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Login successful.')
#                 return redirect('profile')  # Redirect to the profile page
#             else:
#                 messages.error(request, 'Invalid email or password.')

#     else:
#         form = kumbiForm()

#     return render(request, 'login.html', {'form': form})
# def login(request):
#     if request.session.has_key('is_logged'):
#         return redirect('profile')
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user=auth.authenticate(email=email,password=password)


#         if user is not None:

#             auth.login(request, user)
#             request.session['is_logged'] = True
#             return redirect('profile')
#         else:
#             messages.info(request, 'invalid Email or Password')
#             return redirect('login')

#     else:
#         return render(request, 'login.html')


#view.py

# from django.shortcuts import render,redirect
# from .models import Files
# def index(request):
#     if request.method == 'POST':
#         files = request.FILES.getlist('files')
#         file_list = []

#         for file in files:
#             new_file = Files(
#                 file = file
#             )
#             new_file.save()
#             file_list.append(new_file.file.url)

#         return render(request,{'new_urls': file_list})
    

# #model.py
# from django.db import models   
# class Files(models.model):
#     file = models.FileFiels(upload_to='file')

# #html
# <input type="file" multiple name="files" id"name" required/>
# {%for url in new_urls%}
# <img src="{{url}}" width="150" height="150"/>
# {% endfor%}