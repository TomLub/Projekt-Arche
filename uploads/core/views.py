from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Strona Główna')
    return render(request, 'home.html')


def info(request):
    print('Info')
    return render(request, 'info.html')


def quiz(request):
    print('Quiz')
    return render(request, 'quiz.html')


def nauka(request):
    print('Nauka')
    return render(request, 'nauka.html')

def tales(request):
    print('Tales')
    return render(request,'tales.html')

def anaksymander(request):
    print('Anaksymander')
    return render(request,'anaksymander.html')

def anaksymenes(request):
    print('Anaksymenes')
    return render(request,'anaksymenes.html')

def heraklit(request):
    print('Heraklit')
    return render(request,'heraklit.html')

def pitagoras(request):
    print('Pitagoras')
    return render(request,'pitagoras.html')

def parmenides(request):
    print('parmenides')
    return render(request,'parmenides.html')

def empedokles(request):
    print('empedokles')
    return render(request,'empedokles.html')

def anaksagoras(request):
    print('anaksagoras')
    return render(request,'anaksagoras.html')

def demokryt(request):
    print('Demokryt')
    return render(request,'demokryt.html')
