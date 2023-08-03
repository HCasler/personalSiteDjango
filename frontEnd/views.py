from django.shortcuts import render

def index(request):
    return render(request, "frontEnd/index.html", {})

def aboutMe(request):
    return render(request, "frontEnd/contentPages/aboutMe.html", {})

def coding(request):
    return render(request, "frontEnd/contentPages/coding.html", {})

def research(request):
    return render(request, "frontEnd/contentPages/research.html", {})

def publications(request):
    return render(request, "frontEnd/contentPages/publications.html", {})

def contact(request):
    return render(request, "frontEnd/contentPages/contact.html", {})

def comingSoon(request):
    return render(request, "frontEnd/contentPages/comingSoon.html", {})