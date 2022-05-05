from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myfirstapp/index.html')

def bonjour(request):
    nom=request.GET["nom"] # récupère la valeur du paramètre nom du formulaire
    return render(request,'myfirstapp/bonjour.html', {"nom":nom})

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')


def main(request):
    return render(request, 'myfirstapp/main.html')


# route, action et vues formulaire
# route avec action + vue pour le traitement : <form action="/.../.../">