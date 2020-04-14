import unittest
from work import loop_quiz

class TestLoopQuiz(unittest.TestCase):
    def test_loop(self):
        expect = ['Avocado', 'Omelette_rice', 'Apple']
        actual = loop_quiz()
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()