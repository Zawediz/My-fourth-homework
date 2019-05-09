import unittest
import password


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(password.check('Anna12345'), 'weak')

    def test2(self):
        self.assertEqual(password.check('Ann1polk'), 'strong')

    def test3(self):
        self.assertEqual(password.check('AnAnAn11'), 'weak')


if __name__ == '__main__':
    unittest.main()
