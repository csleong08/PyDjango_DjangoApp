from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request,number):
    print(number)
    return HttpResponse("placeholder to display blog " + number)

def edit(request,number):
    print(number)
    return HttpResponse("placeholder to edit blog " + number)

def destroy(request,number):
    return redirect('/')