import unittest
from work import list_quiz

class TestListQuiz(unittest.TestCase):
    def test_append_and_enum(self):
        expect = ['python_lang', 'java_lang', 'go_lang', 'ruby_lang']
        actual = list_quiz()
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()