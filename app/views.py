from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        print("User is already authenticated")
        return HttpResponse("Logged in user")
    else:
        print("Anonymous user")
    return HttpResponse("Anonymous user")


def home(request):
    print('home............')
    return HttpResponse({"Home page"})