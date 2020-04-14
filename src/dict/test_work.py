import unittest
from work import dict_quiz

class TestDictQuiz(unittest.TestCase):
    def test_dict(self):
        expect = {'google': 'GCP', 'microsoft': 'AZURE', 'amazon': 'AWS'}
        actual = dict_quiz()
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()