from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appointment_management.serializers import AppointmentSerializer
from hospital_management.models import Appointment
from django.shortcuts import get_object_or_404
from hospital_management.permissions import IsDoctorOnly, IsPatientOnly
from rest_framework.permissions import AllowAny


class AppointmentViewAPI(APIView):
    permission_classes = [IsPatientOnly]

    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AppointmentDetailViewAPI(APIView):

    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




    