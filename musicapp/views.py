from django.http.response import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(request, "main_page.html")

class GuaranaApp:

    def __init__(self, name):
        self.name = name