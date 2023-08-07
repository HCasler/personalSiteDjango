from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage

class NonexistentResourceTests(TestCase):

    def testNonExistentMainPage(self):
        response = self.client.get("/thisPageDoesNotExist")
        self.assertEqual(response.status_code, 404)
        # should return the top-level nonexistent page
        self.assertIn('<div id="navbar">', str(response.content))


    def testNonExistentSubPage(self):
        response = self.client.get("/contentPages/thisPageDoesNotExist")
        self.assertEqual(response.status_code, 404)
        # this should be a sub-page, not a complete document
        self.assertNotIn('<div id="navbar">', str(response.content))

    def testNonExistentStaticFile(self):
        response = self.client.get(staticfiles_storage.url('frontEnd/images/noSuchImageHere.jpg'))
        self.assertEqual(response.status_code, 404)


class PageExistsTests(TestCase):

    # paths to subpages, and unique elements in each
    allSubPages = {"/contentPages/aboutMe.html":'<div id="aboutMe" class="pageContent">',
        "/contentPages/coding.html": '<div id="softwareEngineering" class="pageContent">',
        "/contentPages/contact.html": '<div id="contact" class="pageContent">',
        "/contentPages/publications.html": '<div id="publications" class="pageContent">',
        "/contentPages/research.html": '<div id="research" class="pageContent">',
    }

    def testMainPageExists(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<div id="navbar">', str(response.content))

    def testSubPagesExist(self):
        for pagePath in self.allSubPages:
            response = self.client.get(pagePath)
            self.assertEqual(response.status_code, 200)
            self.assertIn(self.allSubPages[pagePath], str(response.content))
            self.assertNotIn('<div id="navbar">', str(response.content))



