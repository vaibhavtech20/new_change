from django.urls import path,re_path
from .views import login
from .import views
from .views import dashboard, accept_reject_interest , download_biodata , send_connection_request ,handle_connection_request
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import (
    send_interest,
    chat,
    shortlist,
    profile_detail,
)
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('profile',views.profile, name='profile'),
    path('logout', views.logout, name="logout"),
    path('create_profile', views.create_profile, name='create_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('profile_view/<int:receiver_id>/', views.profile_view, name='profile_view'),
    # path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('accept_reject_interest/<int:interest_id>/<str:action>/', accept_reject_interest, name='accept_reject_interest'),
    path('download-biodata/<int:pk>/', download_biodata, name='download_biodata'),
    path('send-connection-request/<int:receiver_id>/', send_connection_request, name='send_connection_request'),
    path('handle-connection-request/<int:request_id>/<str:action>/', handle_connection_request, name='handle_connection_request'),

    # Password reset views
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
    path('profile/<int:receiver_id>/', profile_detail, name='profile_detail'),
    path('send_interest/<int:receiver_id>/', send_interest, name='send_interest'),
    path('chat/<int:receiver_id>/', chat, name='chat'),
    path('shortlist/<int:profile_id>/', shortlist, name='shortlist'),

    # old 
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),name='password_change_done'),
    # path('password_change/',auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),name='password_change'),
    # path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),

    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
    path('request/<int:request_id>/', views.accept_reject_view_request, name='accept_reject_view_request'),
    path('profile/detail/<int:user_id>/', views.profile_detail1, name='profile_detail1'),


]

