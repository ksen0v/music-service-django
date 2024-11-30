from django.http.response import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(request, "main_page.html")


def login(request):
    return render(request, "login.html")

def sign_up(request):
    return render(request, "sign_up.html")