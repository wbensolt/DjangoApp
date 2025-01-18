from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Apptwo")

def djangorocks(request):
    return HttpResponse("This Two")

def picture_detail(request, category, year = 2000, month = 0):
    body = f"Category = {category}, year = {year}, month = {month}"
    return HttpResponse(body)