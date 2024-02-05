# from django.db import models

# class kumbi(models.Model):
#     gender_choices = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     )

#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)  # Note: In a production environment, use a hashed password field
#     confirmPassword = models.CharField(max_length=100)
#     dob = models.DateField()
#     gender = models.CharField(choices=gender_choices,max_length=120)
#     # Add more fields as needed, such as address, education, occupation, etc.

#     # You might want to add additional fields for verification purposes (e.g., is_verified, verification_code, etc.)

#     def __str__(self):
#         return self.

# models.py

from django.db import models
from django.db.models import BigAutoField
from django.conf import settings

class MatrimonialProfile(models.Model):
    id = BigAutoField(primary_key=True)
    # objects = CustomUserManager()
    # Section 2: Basic Details
    profile_pic = models.ImageField(upload_to='profile_pics/')
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    height = models.FloatField() 
    date_of_birth = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20, choices=[('single', 'Single'), ('married', 'Married')])
    caste = models.CharField(max_length=50, default='Wandekar Kunbi')
    country_living = models.CharField(max_length=50)
    state_living = models.CharField(max_length=50)
    city_living = models.CharField(max_length=50)
    permanent_address = models.TextField()

    # Section 3: About Me
    bio = models.TextField(null=True, blank=True)
    profile_created_by = models.CharField(max_length=50)
    languages_spoken = models.CharField(max_length=100)
    disability = models.BooleanField(default=False)

    # Section 4: Education
    about_education = models.TextField(null=True, blank=True)
    highest_education = models.CharField(max_length=100,null=True, blank=True)
    pg_degree = models.CharField(max_length=100,null=True, blank=True)
    pg_college = models.CharField(max_length=100,null=True, blank=True)
    ug_degree = models.CharField(max_length=100,null=True, blank=True)
    ug_college = models.CharField(max_length=100,null=True, blank=True)
    school_name = models.CharField(max_length=100,null=True, blank=True)

    # Section 5: Career
    about_career = models.TextField(null=True, blank=True)
    employed_in = models.CharField(max_length=100,null=True, blank=True)
    occupation = models.CharField(max_length=100,null=True, blank=True)
    organization_name = models.CharField(max_length=100,null=True, blank=True)

    # Section 6: Family
    about_family = models.TextField(null=True, blank=True)
    father_occupation = models.CharField(max_length=100,null=False, blank=False)
    mother_occupation = models.CharField(max_length=100,null=False, blank=False)
    brothers = models.PositiveIntegerField()
    sisters = models.PositiveIntegerField()
    married_sisters = models.PositiveIntegerField()
    # family_income = models.PositiveIntegerField(null=True, blank=True)
    living_with_parents = models.BooleanField(default=False)
    family_based_city = models.CharField(max_length=50,null=False, blank=False)
    maternal_uncles_name = models.CharField(max_length=100,null=False, blank=False)
    

    # Section 7: Contact Details
    email = models.EmailField(unique=True ,blank=False,null=False)
    phone_no = models.CharField(max_length=15)

    # Section 8: Lifestyle
    lifestyle = models.TextField(null=True, blank=True)
    drinking_habits = models.BooleanField(default=False)
    smoking_habits = models.BooleanField(default=False)

    # section 9 : Document upload
    biodata = models.FileField(upload_to='uploads/', null=True, blank=True)

    # Section 10: Phone Number Visibility
    is_phone_visible = models.BooleanField(default=False)
    
    def __str__(self): 
        return str(self.name)



class Interaction(models.Model):
    sender = models.ForeignKey(MatrimonialProfile, on_delete=models.CASCADE, related_name='sent_interactions')
    receiver = models.ForeignKey(MatrimonialProfile, on_delete=models.CASCADE, related_name='received_interactions')
    action = models.CharField(max_length=20)  # 'interest', 'shortlist', 'chat', 'ignore'
    timestamp = models.DateTimeField(auto_now_add=True)
# class YourImageModel(models.Model):
#     image = models.ImageField(upload_to='profile_pics/')
#     # You can add additional fields like description, date uploaded, etc.

#     def __str__(self):
#         return str(self.image)


    
