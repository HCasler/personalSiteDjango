from django.shortcuts import render
import logging
from django.template.exceptions import TemplateDoesNotExist

logger = logging.getLogger(__name__)

def index(request):
    logger.debug("received {0} request for index page".format(request.method))
    try: 
        return render(request, "frontEnd/index.html", {})
    except TemplateDoesNotExist:
        logger.critical("Failed to retrieve template frontEnd/index.html")
        return nonexistent(request, 'frontEnd/index.html')

def aboutMe(request):
    logger.debug("received {0} request for about-me page".format(request.method))
    try:
        return render(request, "frontEnd/contentPages/aboutMe.html", {})
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template frontEnd/contentPages/aboutMe.html")
        return nonexistentSubpage(request, 'frontEnd/contentPages/aboutMe.html')

def coding(request):
    logger.debug("received {0} request for coding page".format(request.method))
    try:
        return render(request, "frontEnd/contentPages/coding.html", {})
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template frontEnd/contentPages/coding.html")
        return nonexistentSubpage(request, 'frontEnd/contentPages/coding.html')

def research(request):
    logger.debug("received {0} request for research page".format(request.method))
    try:
        return render(request, "frontEnd/contentPages/research.html", {})
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template frontEnd/contentPages/research.html")
        return nonexistentSubpage(request, 'frontEnd/contentPages/research.html')

def publications(request):
    logger.debug("received {0} request for publications page".format(request.method))
    try:
        return render(request, "frontEnd/contentPages/publications.html", {})
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template frontEnd/contentPages/publications.html")
        return nonexistentSubpage(request, 'frontEnd/contentPages/publications.html')

def contact(request):
    logger.debug("received {0} request for contact page".format(request.method))
    try:
        return render(request, "frontEnd/contentPages/contact.html", {})
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template frontEnd/contentPages/contact.html")
        return nonexistentSubpage(request, 'frontEnd/contentPages/contact.html')

def comingSoon(request):
    logger.debug("received {0} request for coming-soon page".format(request.method))
    try:
        return render(request, "frontEnd/contentPages/comingSoon.html", {})
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template frontEnd/contentPages/comingSoon.html")
        return nonexistentSubpage(request, 'frontEnd/contentPages/comingSoon.html')

def nonexistentSubpage(request, other_path):
    logger.error("received {0} request for nonexistent path {1}".format(request.method, other_path))
    resp = render(request, "frontEnd/contentPages/nonexistentSubpage.html", {})
    resp.status_code = 404
    return resp

def nonexistent(request, other_path):
    logger.error("received {0} request for nonexistent path {1}".format(request.method, other_path))
    resp = render(request, "frontEnd/nonexistent.html", {})
    resp.status_code = 404
    return resp

