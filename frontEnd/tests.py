from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your tests here.

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

