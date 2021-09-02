from django.shortcuts import render

def home(request):
    return render(request, 'api/home.html')

def about(request):
    return render(request, 'api/about.html')
