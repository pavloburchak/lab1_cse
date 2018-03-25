import unittest
import url

class TestLab1(unittest.TestCase):
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
 
    def test_get_filename(self):
        self.assertEqual(url.get_filename("/error"), None)
        self.assertEqual(url.get_filename("Content-Disposition: attachment; filename=filename.mp3"), "filename.mp3")
        self.assertEqual(url.get_filename("Content-Disposition: attachment; filename="), None)
    def test_download_mp3(self):
        link1 = "https://res.cloudinary.com/hvldskieo/raw/upload/v1521464696/01_Stuck_on_the_puzzle_intro_osli5a.mp3"
        link2 = "https://res.cloudinary.com/hvldskieo/raw/upload/v1521464696/01_Stuck_on_the_puzzle_intro_osli5a"
        self.assertEqual(url.download_mp3(link1, 2017), "01_Stuck_on_the_puzzle_intro_osli5a.mp3")
        self.assertEqual(url.download_mp3(link2, 2017), None)
    def test_get_urls(self):
        linkTrue = "http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/"
        linkFalse = "http://turing.plymouth.edu/~zshen/Webfiles/notes/CS130/PythonExamples/jscript.html"
        self.assertTrue(url.get_urls(linkTrue, 1, 2017))
        self.assertFalse(url.get_urls(linkFalse, 1, 2017))
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab1)
    unittest.TextTestRunner(verbosity=2).run(suite)