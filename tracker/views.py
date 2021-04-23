from django.shortcuts import render,get_object_or_404
from .models import Patient

def home(request):
    patients = Patient.objects.all()
    return render(request, 'vaccinated/home.html', {'patients': patients,})

def patient(request, patient_id):
    patient=get_object_or_404(Patient, pk=patient_id)
    patients=Patient.objects.all()
    return render(request,'vaccinated/patient.html',{'patient':patient,'patients':patients,})

# Create your views here.
