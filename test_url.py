import unittest

class TestLab1(unittest.TestCase):
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
 
    def test_get_filename(self):
        self.assertEqual(get_filename("/error"), None)
        self.assertEqual(get_filename("Content-Disposition: attachment; filename=filename.mp3"), "filename.mp3")
        self.assertEqual(get_filename("Content-Disposition: attachment; filename="), None)
    def test_download_mp3(self):
        link1 = "https://res.cloudinary.com/hvldskieo/raw/upload/v1521464696/01_Stuck_on_the_puzzle_intro_osli5a.mp3"
        link2 = "https://res.cloudinary.com/hvldskieo/raw/upload/v1521464696/01_Stuck_on_the_puzzle_intro_osli5a"
        self.assertEqual(download_mp3(link1, 2017), "01_Stuck_on_the_puzzle_intro_osli5a.mp3")
        self.assertEqual(download_mp3(link2, 2017), None)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab1)
    unittest.TextTestRunner(verbosity=2).run(suite)