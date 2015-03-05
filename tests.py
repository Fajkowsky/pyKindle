import unittest


class BasicTest(unittest.TestCase):
    def test_dumb(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()