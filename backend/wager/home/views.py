from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

def display(request):
    return render(request, 'Survey.html')