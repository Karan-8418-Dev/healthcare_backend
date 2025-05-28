from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorCreateSerializer
from patients.models import Patient

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return PatientDoctorCreateSerializer
        return PatientDoctorMappingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # SECURITY: Check patient ownership
        patient = serializer.validated_data['patient']
        if patient.created_by != request.user:
            return Response({'error': 'Access denied'}, status=403)
        
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def by_patient(self, request, patient_id=None):
        # SECURITY: Required for assignment endpoint GET /api/mappings/<patient_id>/
        try:
            patient = Patient.objects.get(id=patient_id, created_by=request.user)
            mappings = PatientDoctorMapping.objects.filter(patient=patient)
            serializer = self.get_serializer(mappings, many=True)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)