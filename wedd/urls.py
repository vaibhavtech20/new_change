from django.urls import path,re_path
from .views import login
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('profile',views.profile, name='profile'),
    path('logout', views.logout, name="logout"),
    path('create_profile', views.create_profile, name='create_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    # path('profile/<int:profile_id>/', views.profile, name='profile'),
    

    # Password reset views
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
     re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    


    # old 
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),name='password_change_done'),
    # path('password_change/',auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),name='password_change'),
    # path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),


]

