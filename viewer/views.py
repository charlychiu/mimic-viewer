from django.shortcuts import render
from . import views
from .models import *

# Create your views here.

def index(request):
    # a = Admissions.objects.all()
    # print(a[0].subject.subject_id)
    b = Patients.objects.all()
    print(b[0].admissions_set.all()[0].admittime)
    pass