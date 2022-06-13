from django.shortcuts import render

def home(request):
    return render(request, 'projects/home.html')

def detail(request,pk):
    return render(request, 'projects/detail.html')
