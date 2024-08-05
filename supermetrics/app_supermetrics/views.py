from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse

def dashboard(request: HttpRequest):

    dados = {}
    return render(request , "dashboard.html", dados)
