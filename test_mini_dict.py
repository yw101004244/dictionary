from mini_dict import handle_input,SearchDictionary
import unittest

class MiniDictionaryTestCase(unittest.TestCase):
    def test_blank(self):
        '''能否正确处理空白输入'''
        search = SearchDictionary()
        tip = search.search_all("\n")
        self.assertEqual(tip,"input error")

    def test_in(self):
        '''能否正常处理在字典中的单词'''
        search = SearchDictionary()
        tip = search.search_all("discuss\n")
        self.assertNotEqual("input error",tip)

    def test_not_in(self):
        '''能否正常处理不在字典中的单词'''
        search = SearchDictionary()
        tip = search.search_all("12313dwdad\n")
        self.assertEqual("input error",tip)

unittest.main()






'''
usr_input = input("Please input a word: ")
usr_input = handle_input(usr_input)

dictionary=SearchDictionary()
dictionary.search_soundmark(usr_input) #查询音标
dictionary.search_character(usr_input) #查询词性
dictionary.search_explaination(usr_input) #查询解释
dictionary.search_all(usr_input) #查询解释'''