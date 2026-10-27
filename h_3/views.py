from django.shortcuts import render

from h_3.models import Student

# Create your views here.
def home(request):
    students = Student.objects.all() # جلب البيانات من قاعدة البيانات
    return render(request, 'home.html', {'students': students})