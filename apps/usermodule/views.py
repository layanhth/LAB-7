from django.shortcuts import render
from django.db.models import Count
from .models import Student

def students_by_city(request):
    data = Student.objects.values('address__city').annotate(total=Count('id'))
    return render(request, 'bookmodule/lab8_task7.html', {'data': data})
