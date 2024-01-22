# from django.contrib import admin 
# from .models import kumbi


# # Register your models here.

# class KumbiAdmin(admin.ModelAdmin):
#     list_display = ("full_name", "email","password","confirmPassword","dob","gender",)


# admin.site.register(kumbi,KumbiAdmin)

from django.contrib import admin
from .models import MatrimonialProfile

class MatrimonialProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_pics','name', 'gender','height','date_of_birth','birth_time','birth_place', 'marital_status','caste','country_living','state_living','city_living','permanent_address','bio','profile_created_by','languages_spoken','disability','about_education','highest_education','pg_degree','pg_college','ug_degree','ug_college','school_name','about_career','employed_in','occupation','organization_name','about_family','father_occupation','mother_occupation','brothers','sisters','married_sisters','living_with_parents','family_based_city','maternal_uncles_name', 'email_id', 'phone_no','lifestyle','drinking_habits','smoking_habits','biodata')
    search_fields = ('name', 'email_id','gender','height','date_of_birth' )
    list_filter = ('gender', 'marital_status', 'city_living','height','date_of_birth')

admin.site.register(MatrimonialProfile, MatrimonialProfileAdmin)

