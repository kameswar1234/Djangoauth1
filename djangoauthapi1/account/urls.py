from django.urls import path
from account.views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,\
    SendPasswordRestEmailView,UserPasswordResetView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('send_reset_password_email/',SendPasswordRestEmailView.as_view(),name='send-reset-password-email'),
    path('reset_password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
]