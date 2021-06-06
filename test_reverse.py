import unittest
import reverse
import pytest

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse.string_reverse("hi my name is katie"),"katie is name my hi")

    def test_2(self):
        self.assertEqual(reverse.string_reverse("1 2 3 4 5"),"5 4 3 2 1")

    def test_3(self):
        self.assertEqual(reverse.string_reverse(65432),-1)

if __name__ == '__main__': 
    unittest.main(verbosity=2) 