import unittest 
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tim", self.guest_1.name)

    def test_guest_has_name(self):
        self.assertEqual("Tim", self.guest_1.name)