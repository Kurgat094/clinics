from django.urls import path
from .views import *



urlpatterns = [
    path("",home,name="Home"),
    path("signin/",signin,name="Login"),
    path("signup/",signup,name="Register"),
    path("forgotpassword/",forgotpassword,name="Forgot Password"),
]