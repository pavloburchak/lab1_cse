import url
import requests
import unittest

class TestLab1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_defined_file(self):
        link = 'https://res.cloudinary.com/hvldskieo/raw/upload/v1514037636/' + \
        '08._Writer_In_the_Dark_d7e0kn.mp3'
        filename = '08._Writer_In_the_Dark_d7e0kn.mp3'
        r = requests.get(link, allow_redirects=True)
        self.assertTrue(url.save_defined_file(filename, 2016, r))
        self.assertFalse(url.save_defined_file(filename, 2048, r))

    def test_download_mp3(self):
        link1 = 'https://res.cloudinary.com/hvldskieo/raw/upload/v1514037636/' + \
        '08._Writer_In_the_Dark_d7e0kn.mp3'
        link2 = 'https://res.cloudinary.com/hvldskieo/raw/upload/v1514037631/' + \
        '05._Liability_qt1tdv'
        self.assertEqual(url.download_mp3(link1, 2016), '08._Writer_In_the_Dark_d7e0kn.mp3')
        self.assertEqual(url.download_mp3(link2, 2016), None)

    def test_get_filename(self):
        self.assertEqual(url.get_filename(None), None)
        self.assertEqual(url.get_filename('/error'), None)
        self.assertEqual(url.get_filename('Content-Disposition: attachment; fil' + \
        'ename=filename.mp3'), 'filename.mp3')
        self.assertEqual(url.get_filename('Content-Disposition: attachment; fil' + \
        'ename='), None)

    def test_get_urls(self):
        linkTrue = 'http://www.patricksoftwareblog.com/python-unit-testing-stru' + \
        'cturing-your-project/'
        linkFalse = 'http://turing.plymouth.edu/~zshen/Webfiles/notes/CS130/Pyt' + \
        'honExamples/jscript.html'
        self.assertTrue(url.get_urls(linkTrue, 1, 2017))
        self.assertFalse(url.get_urls(linkFalse, 1, 2017))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab1)
    unittest.TextTestRunner(verbosity=2).run(suite)
