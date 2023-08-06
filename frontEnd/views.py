from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.debug("received {0} request for index page".format(request.method))
    return render(request, "frontEnd/index.html", {})

def aboutMe(request):
    logger.debug("received {0} request for about-me page".format(request.method))
    return render(request, "frontEnd/contentPages/aboutMe.html", {})

def coding(request):
    logger.debug("received {0} request for coding page".format(request.method))
    return render(request, "frontEnd/contentPages/coding.html", {})

def research(request):
    logger.debug("received {0} request for research page".format(request.method))
    return render(request, "frontEnd/contentPages/research.html", {})

def publications(request):
    logger.debug("received {0} request for publications page".format(request.method))
    return render(request, "frontEnd/contentPages/publications.html", {})

def contact(request):
    logger.debug("received {0} request for contact page".format(request.method))
    return render(request, "frontEnd/contentPages/contact.html", {})

def comingSoon(request):
    logger.debug("received {0} request for coming-soon page".format(request.method))
    return render(request, "frontEnd/contentPages/comingSoon.html", {})

def nonexistent(request, other_path):
    logger.error("received {0} request for nonexistent path {1}".format(request.method, other_path))
    resp = render(request, "frontEnd/contentPages/nonexistent.html", {})
    resp.status_code = 404
    return resp

