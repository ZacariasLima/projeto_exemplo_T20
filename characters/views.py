from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'characters/pages/home.html', context= {
        'name': 'Zacarias Figueiredo Lima',
    })

# Character detail
def character (request, id):
    return render (request, 'characters/pages/character-view.html', context= {
        'name': 'Zacarias Figueiredo Lima',
        })