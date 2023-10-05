from django.urls import path
from .views import signupView, signupController, loginView, loginController, logoutController

urlpatterns = [
    path('signup', signupView, name='signup'),
    path('register', signupController),
    path('login', loginView, name='loginView'),
    path('authenticate', loginController, name='authenticate'),
    path('logout', logoutController, name='logout')
]