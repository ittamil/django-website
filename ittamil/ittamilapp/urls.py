from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView


urlpatterns = [
    path("", views.PostView, name="index"),
    path('accounts/profile/',views.profile, name='profile'),
    path('profile/edit_profile',views.edit_profile, name='edit_profile'),    
    path('signup/',views.signup, name='signup'),
    path('ittamilapp/login/',LoginView.as_view(), name='login'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='index'), name='logout'),
    path('password_reset/',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset/complete',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("<slug:slug>/" , views.PostDetailView, name="PostDetailView"),
  
    
]