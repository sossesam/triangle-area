
from django.shortcuts import render
from . import perimeter



def home(request):
    return render(request,'index.html')

def result(request):
    name = request.GET['user_name']
    side1=request.GET['side1']
    side2=request.GET['side2']
    side3=request.GET['side3']
    result = perimeter.triangle_area(side1,side2,side3)
    return render(request,'result.html', {'result':result, 'name':name})