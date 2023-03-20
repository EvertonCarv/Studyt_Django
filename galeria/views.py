from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')