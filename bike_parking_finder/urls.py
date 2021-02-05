"""bike_parking_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Homef
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.views import VerifyEmailView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

urlpatterns = [
    path('bikeadmin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/', include('dj_rest_auth.urls'), name="e_login"),
    path("auth/facebook/", FacebookLogin.as_view(), name="fb_login"),
    path("auth/google/", GoogleLogin.as_view(), name="g_login"),
    path('auth/register/', include('dj_rest_auth.registration.urls'), name="register"),
    path("auth/register/account-confirm-email/", VerifyEmailView.as_view(), name="account-confirm-email")
]
