from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome To Home Page of sn_codeLab")
    return render(request,'webpage/index.html')

def about(request):
    # return HttpResponse("Welcome to About Page of sn_codeLab")
    return render(request,'webpage/about.html')

def contact(request):
    # return HttpResponse("Welcome to contact Page of sn_codeLab")
     return render(request,'webpage/contact.html')

def services(request):
    # return HttpResponse("Welcome to services Page of sn_codeLab")
     return render(request,'webpage/services.html')