from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.request.query_params.get('patient_id')

        if patient_id:
            return PatientDoctorMapping.objects.filter(patient_id=patient_id)

        return PatientDoctorMapping.objects.all()