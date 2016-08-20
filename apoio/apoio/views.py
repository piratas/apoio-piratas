from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'SIGLA': 'PARTIDO PIRATA', 'NOME': 'Campanha de Coleta de Assinaturas'})

def volunteer(request):
    return render(request, 'volunteer.html')
