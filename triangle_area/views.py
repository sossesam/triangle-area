
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def result(request):
    name = request.GET['user_name']
    return render(request,'result.html', {'result':name})