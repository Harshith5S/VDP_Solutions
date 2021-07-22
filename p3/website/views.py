from django.contrib import messages
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def startpage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def tea(request):
    return render(request,'tea.html')

def galis(request):
    return render(request,'galis.html')

def fairandlovely(request):
    return render(request,'fairandlovely.html')

def cigarette(request):
    return render(request,'cigarette.html')

def biscuit(request):
    return render(request,'biscuit.html')

def panaka(request):
    return render(request,'panaka.html')


def teaform(request):
    if request.POST:
        rate = request.POST['rate']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO review VALUES('Tea','" +rate+ "','" +message+ "');")
        messages.error(request, 'Review Submitted.')
        return HttpResponseRedirect(reverse('tea'))

def galisform(request):
    if request.POST:
        rate = request.POST['rate']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO review VALUES('Galis','" +rate+ "','" +message+ "');")
        messages.error(request, 'Review Submitted.')
        return HttpResponseRedirect(reverse('galis'))

def fairandlovelyform(request):
    if request.POST:
        rate = request.POST['rate']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO review VALUES('Fair And Lovely','" +rate+ "','" +message+ "');")
        messages.error(request, 'Review Submitted.')
        return HttpResponseRedirect(reverse('fairandlovely'))

def cigaretteform(request):
    if request.POST:
        rate = request.POST['rate']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO review VALUES('Cigarette','" + rate + "','" + message + "');")
        messages.error(request, 'Review Submitted.')
        return HttpResponseRedirect(reverse('cigarette'))

def biscuitform(request):
    if request.POST:
        rate = request.POST['rate']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO review VALUES('Biscuit','" +rate+ "','" +message+ "');")
        messages.error(request, 'Review Submitted.')
        return HttpResponseRedirect(reverse('biscuit'))

def panakaform(request):
    if request.POST:
        rate = request.POST['rate']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO review VALUES('Panaka','" +rate+ "','" +message+ "');")
        messages.error(request, 'Review Submitted.')
        return HttpResponseRedirect(reverse('panaka'))

def contactform(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        subject = request.POST['subject']
        message = request.POST['message']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contact VALUES('"+name+"','" +email+ "','"+phno+"','"+subject+"','" +message+ "');")
        messages.error(request, 'Successfully Submitted.')
        return HttpResponseRedirect(reverse('contact'))