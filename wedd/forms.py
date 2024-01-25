# from django import forms
# from django.forms import ModelForm
# from .models import kumbi

# #Create a iplist form

# class kumbiForm(ModelForm):
#     class Meta:
#         model = kumbi
#         fields = ('full_name','email','password','confirmPassword','dob','gender')

#         labels = {
#             'full_name' : '',
#             'email' :'',
#             'password' : '',
#             'confirmPassword' : '',
#             'dob' :'',
#             'gender' : 'Gender',
            
#         }

#         widgets = {
            
#             # 'group' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Group'}),
#             # 'group' : forms.ChoiceField( choices=[group_choices], required=False),
#             'full_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your full name'}),
#             # 'site' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Site'}),
#             'email' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'email'}),
#             'password' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your password'}),
#             'confirmPassword' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Confirm your password'}),
#             'dob' : forms.DateInput(attrs={'class' : 'form-control','placeholder' : 'Date of Birth'}),
#         }

# from django import forms
# from .models import MatrimonialProfile

# class MatrimonialProfileForm(forms.ModelForm):
#     class Meta:
#         model = MatrimonialProfile
#         fields = '__all__'
#         widgets = {
#             'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
#         }

# forms.py

from django import forms
# from extra_views import ClearableFileInput                  #this is after install django-extra-views
from .models import MatrimonialProfile,YourImageModel  
from django.core.validators import FileExtensionValidator

class TimePickerWidget(forms.TextInput):
    input_type = 'time'

class MatrimonialProfileForm(forms.ModelForm):
    class Meta:
        model = MatrimonialProfile
        fields = ['name','gender','height','date_of_birth','birth_time','birth_place','marital_status','caste','country_living','state_living','city_living','permanent_address','bio','profile_created_by','languages_spoken','disability','about_education','highest_education','pg_degree','pg_college','ug_degree','ug_college','school_name','about_career','employed_in','occupation','organization_name','about_family','father_occupation','mother_occupation','brothers','sisters','married_sisters','living_with_parents','family_based_city','maternal_uncles_name','email','phone_no','lifestyle','drinking_habits','smoking_habits','biodata']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # 'birth_time': forms.TimeInput(attrs={'type': 'time'}),
            # 'profile_pics': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    # profilePics = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
    # profile_pics = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'multiple': True}))
    
    # Basic Details
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}), required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    height = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter height'}), required=True)

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    birth_time = forms.TimeField(widget=TimePickerWidget)
    # birth_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}), required=True)
    birth_place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter birth place'}), required=True)
    marital_status = forms.ChoiceField(choices=[('single', 'Single'), ('married', 'Married')], widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    # caste = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, required=True)
    caste = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, required=True, initial='Wandekar Kunbi')
    country_living = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,initial='India')
    state_living = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, initial='Maharashtra')
    city_living = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, required=True)
    permanent_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter permanent address'}), required=False)
   
    # About Me
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter bio'}), required=False)
    profile_created_by = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter profile created by'}), required=True)
    languages_spoken = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter languages spoken'}), required=False)
    # disability = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)

    # Education
    about_education = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter information about education'}), required=False)
    highest_education = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter highest education'}), required=False)
    pg_degree = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter postgraduate degree'}), required=False)
    pg_college = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter postgraduate college'}), required=False)
    ug_degree = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter undergraduate degree'}), required=False)
    ug_college = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter undergraduate college'}), required=False)
    school_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name'}), required=False)
   
    # Career
    about_career = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)
    employed_in = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    organization_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)


    # Family
    about_family = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)
    father_occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=True)
    mother_occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=True)
    brothers = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    sisters = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    married_sisters = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    # living_with_parents = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    family_based_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, required=True)
    maternal_uncles_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=True)
    # Contact Details
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=15, required=True)

    lifestyle = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)
    # drinking_habits = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    # smoking_habits = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    # document = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)
    biodata = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )


# class ProfilePictureForm(forms.ModelForm):
#     class Meta:
#         model = MatrimonialProfile
#         fields = ['profile_pics']
#         profile_pics = forms.ManyToManyField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
        # widget={'profile_pics': forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False}
        # widgets = {
        #     'profile_pics': forms.ClearableFileInput(attrs={'multiple': True}),
        # }
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = YourImageModel
        fields = ['image']
        # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
        clear_selection = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'onclick': 'clearFileInput()'})
    )