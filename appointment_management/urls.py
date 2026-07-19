from django.urls import path, include
from appointment_management.views import AppointmentViewAPI, AppointmentDetailViewAPI

# appointments/
urlpatterns = [
    path('', AppointmentViewAPI.as_view(), name='appointment-list'),
    path('', AppointmentViewAPI.as_view(), name='appointment-create'),


    path('<int:pk>/', AppointmentDetailViewAPI.as_view(), name='appointment-view'),


]
