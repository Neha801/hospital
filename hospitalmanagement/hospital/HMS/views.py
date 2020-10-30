from django.shortcuts import render
from django.http import HttpResponse

def Navbar(request):
    return render(request, 'HMS/Navbar.html')

def visitor(request):
    return render(request, 'HMS/visitor.html')

def Infrastructure(request):
    return render(request, 'HMS/Infrastructure.html')

def about(request):
    return render(request, 'HMS/about.html')

def carrer(request):
    return render(request, 'HMS/carrer.html')

def contact(request):
    return render(request, 'HMS/contact.html')

def appointment(request):
    return render(request, 'HMS/appointment.html')

def insurance(request):
    return render(request, 'HMS/insurance.html')

def checkup(request):
    return render(request, 'HMS/checkup.html')

def special(request):
    return render(request, 'HMS/special.html')
