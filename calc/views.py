from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'rami'})

def operation(request):

    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    operation=request.GET['operation']
    if operation=='Add':
        result=val1+val2
    else:
        result=val1-val2
    return render(request,'result.html',{'Result':result})