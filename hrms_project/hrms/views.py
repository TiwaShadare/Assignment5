from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Welcome to the Human Resource Management System API"})
# Create your views here.
