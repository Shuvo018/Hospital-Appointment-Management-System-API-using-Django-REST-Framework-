from hospital_management.serializers import DoctorSerializer, AppointmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hospital_management.models import Doctor, User, Appointment
from django.shortcuts import get_object_or_404
from hospital_management.permissions import IsDoctorOnly
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class FilterDoctorViewAPI(APIView):
    
    def get(self, request):
        query = Doctor.objects.all()
        dept = request.query_params.get('department')
        doctor_id = request.query_params.get('doctor')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        page = request.query_params.get('page')
        
        if dept:
            query = query.filter(department=dept)
        elif doctor_id:
            query = query.filter(id=doctor_id)
        elif search:
            query = query.filter(name__icontains=search)
        elif ordering:
            query = query.order_by(ordering)
        elif page:
            query = query.order_by(ordering)
        
        paginator = PageNumberPagination()
        paginator.page_size = 2
        page = paginator.paginate_queryset(query, request=request)


        serializer = DoctorSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FilterAppointmentViewAPI(APIView):
    
    def get(self, request):
        query = Appointment.objects.all()
        status = request.query_params.get('status')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        
        if status:
            query = query.filter(status=status)
        elif search:
            # query = User.objects.filter(firstname__icontains=search)
            pass

        elif ordering:
            query = query.order_by(ordering)

        paginator = PageNumberPagination()
        paginator.page_size = 2
        page = paginator.paginate_queryset(query, request=request)

        serializer = AppointmentSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)