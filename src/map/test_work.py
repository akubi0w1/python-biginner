import unittest
from work import map_quiz

class TestMapQuiz(unittest.TestCase):
    def test_map(self):
        expect = ['omelette-rice', 'green-pepper', 'ice-cream']
        actual = map_quiz()
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()