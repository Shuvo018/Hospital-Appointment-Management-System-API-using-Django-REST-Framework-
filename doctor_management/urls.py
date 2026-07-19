from django.urls import path, include
from .views import DoctorAPIView
urlpatterns = [
    path('', DoctorAPIView.as_view(), name='doctor-list'),
    path('create/', DoctorAPIView.as_view()),
]