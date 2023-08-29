from django.shortcuts import render
import logging
from django.template.exceptions import TemplateDoesNotExist

logger = logging.getLogger(__name__)

def returnSubPageOr404(request, templatePath, context):
    try:
        return render(request, templatePath, context)
    except TemplateDoesNotExist:
        logger.error("Failed to retrieve template {0}".format(templatePath))
        return nonexistentSubpage(request, request.path)
    except Exception as err:
        logger.error("Failed to retrieve {0} with context {1}:\n{2}".format(templatePath, context, err))
        return err500(request)

# ~~~~ actual views start here ~~~~ #

def index(request):
    logger.debug("received {0} request for index page".format(request.method))
    try: 
        return render(request, "frontEnd/index.html", {})
    except TemplateDoesNotExist:
        logger.critical("Failed to retrieve template frontEnd/index.html")
        return nonexistent(request, 'frontEnd/index.html')
    except Exception as err:
        logger.error("Failed to retrieve {0} with context {1}:\n{2}".format(templatePath, context, err))
        return err500(request)

# ~~~ content sub-pages ~~~ #

def aboutMe(request):
    logger.debug("received {0} request for about-me page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/aboutMe.html", {})

def coding(request):
    logger.debug("received {0} request for coding page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/coding.html", {})

def research(request):
    logger.debug("received {0} request for research page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/research.html", {})

def publications(request):
    logger.debug("received {0} request for publications page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/publications.html", {})

def contact(request):
    logger.debug("received {0} request for contact page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/contact.html", {})

def videoDemo(request):
    logger.debug("received {0} request for video demo page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/videoDemo.html", {})

def comingSoon(request):
    logger.debug("received {0} request for coming-soon page".format(request.method))
    return returnSubPageOr404(request, "frontEnd/contentPages/cominSoon.html", {})

# ~~~ error pages ~~~ #

def nonexistentSubpage(request, other_path=None):
    logger.error("received {0} request for nonexistent path {1}".format(request.method, other_path))
    context = {"missingThing": request.path}
    logger.error(context)
    resp = render(request, "frontEnd/contentPages/nonexistentSubpage.html", context)
    resp.status_code = 404
    return resp

def nonexistent(request, other_path):
    if 'HTTP_X_LOAD_AS_SUBPAGE' in request.META and request.META['HTTP_X_LOAD_AS_SUBPAGE']:
        return nonexistentSubpage(request, other_path)
    else:
        logger.error("received {0} request for nonexistent path {1}".format(request.method, other_path))
        resp = render(request, "frontEnd/nonexistent.html", {})
        resp.status_code = 404
        return resp

def err500(request):
    resp = render(request, "frontEnd/500.html", {})
    resp.status_code = 500
    return resp


def defaultSubPage(request):
    return aboutMe(request)