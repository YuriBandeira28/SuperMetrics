from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse
from banco_funcs import get_df

def dashboard(request: HttpRequest):

    
    return render(request , "dashboard.html", dados)
