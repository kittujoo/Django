from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hellow world!")
    return render(request, 'home.html',{'name':'Krushna'})

def add(request):
    return render(request, 'add.html')

def result(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)
    return render(request, 'result.html',{'result': res, 'res': float(res)})