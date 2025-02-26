from django.urls import path
from .views import RegisterUser, LoginUser, ReferralLink, ReferralStats, ForgotPassword, ResetPassword

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),

]

