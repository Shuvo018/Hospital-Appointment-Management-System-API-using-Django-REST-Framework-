
from django.urls import path
from accounts.views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

]