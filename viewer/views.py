from django.shortcuts import render
from . import views
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    # a = Admissions.objects.all()
    # print(a[0].subject.subject_id)
    patients = Patients.objects.all().prefetch_related('admissions_set')
    fields = Patients._meta.get_fields()

    paginator = Paginator(patients, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # return render(request, 'list.html', {'page_obj': page_obj})

    return render(request, 'viewer/index.html', {'page_obj': page_obj, 'fields': fields})
    # print(b[0].admissions_set.all()[0].admittime)
    # pass