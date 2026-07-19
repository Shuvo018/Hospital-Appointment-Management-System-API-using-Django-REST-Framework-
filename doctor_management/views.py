from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctor_management.serializers import DoctorSerializer, DoctorCreateSerializer
from hospital_management.models import Doctor
from django.shortcuts import get_object_or_404


class DoctorAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DoctorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetailAPIView(APIView):
    def get(self, request, pk):
        print(pk)
        doctor = get_object_or_404(Doctor, id=id)
        print(doctor)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
