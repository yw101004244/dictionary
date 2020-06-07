from search_in_a_dictionary_json import search_in_a_dictionary
import unittest

class DictionaryTestCase(unittest.TestCase):
    def test_blank(self):
        '''能否正确处理空白输入'''
        tip = search_in_a_dictionary("\n")
        self.assertEqual(tip,"input error")

    def test_input_q(self):
        '''能否正确处理q'''
        tip = search_in_a_dictionary("q\n")
        self.assertEqual(tip,0)

    def test_in(self):
        '''能否正常处理在字典中的单词'''
        tip = search_in_a_dictionary("apple\n")
        self.assertIn('apple',tip)

    def test_not_in(self):
        '''能否正常处理不在字典中的单词'''
        tip = search_in_a_dictionary("12313dwdad\n")
        self.assertEqual("input error",tip)

unittest.main()