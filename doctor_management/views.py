from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctor_management.serializers import CreateDoctorSerializer, DoctorListSerializer
from hospital_management.models import Doctor

class DoctorAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CreateDoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

