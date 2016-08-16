import unittest

from core import reverse_hash


class TestReverseHash(unittest.TestCase):
    def setUp(self):
        self.fixtures = [
            {680131659347: 'leepadg'}
        ]

    def test_reverse_hash(self):
        for fixture in self.fixtures:
            for k, v in fixture.iteritems():
                self.assertEqual(reverse_hash(k), v)

if __name__ == '__main__':
    unittest.main()
