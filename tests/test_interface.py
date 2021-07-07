import unittest

#from project.interface import display_news

from project.interface import display_news


class test_interface(unittest.TestCase):

    def test_interface_data(self):
        self.assertEqual(display_news(), 200)
