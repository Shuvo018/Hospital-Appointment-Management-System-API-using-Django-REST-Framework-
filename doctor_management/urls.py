from django.urls import path, include
from .views import DoctorAPIView, DoctorDetailAPIView

# doctors/
urlpatterns = [
    path('', DoctorAPIView.as_view(), name='doctor-list'),
    path('create/', DoctorAPIView.as_view(), name='create-doctor'),

    path('<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-details')

]