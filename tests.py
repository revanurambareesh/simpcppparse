import unittest
import parse

__author__ = 'Ambareesh Revanur'

class TestStringMethods(unittest.TestCase):

    def test_if(self):
        lex_outputfile='tc/if.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_ifel(self):
        lex_outputfile='tc/ifel.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_for(self):
        lex_outputfile='tc/for.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_for(self):
        lex_outputfile='tc/expr.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))    



if __name__ == '__main__':
    unittest.main()