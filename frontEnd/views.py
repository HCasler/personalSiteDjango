from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.debug("received request for index page")
    return render(request, "frontEnd/index.html", {})

def aboutMe(request):
    logger.debug("received request for about-me page")
    return render(request, "frontEnd/contentPages/aboutMe.html", {})

def coding(request):
    logger.debug("received request for coding page")
    logger.info("info message")
    return render(request, "frontEnd/contentPages/coding.html", {})

def research(request):
    logger.debug("received request for research page")
    return render(request, "frontEnd/contentPages/research.html", {})

def publications(request):
    logger.debug("received request for publications page")
    return render(request, "frontEnd/contentPages/publications.html", {})

def contact(request):
    logger.debug("received request for contact page")
    return render(request, "frontEnd/contentPages/contact.html", {})

def comingSoon(request):
    logger.debug("received request for coming-soon page")
    return render(request, "frontEnd/contentPages/comingSoon.html", {})
