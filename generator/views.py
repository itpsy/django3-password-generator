from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('1234567890')
    special_chars = list(r'!"§$%&/()=?*ÄÖÜ-_:.;,<>|^°+~\{[]}öüä´`')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list(r'!"§$%&/()=?*ÄÖÜ-_:.;,<>|^°+~\{[]}öüä´`'))

    length = int(request.GET.get('length', 15))

    passwd = ''
    for x in range(length):
        passwd += random.choice(characters)
    return render(request, 'generator/password.html', {'password': passwd})


def about(request):
    return render(request, 'generator/about.html')
