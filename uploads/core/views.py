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
