import unittest
import parse

__author__ = 'Ambareesh Revanur'

class TestParser(unittest.TestCase):

    def test_if(self):
        lex_outputfile='tc/if.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_ifel(self):
        lex_outputfile='tc/ifel.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_for(self):
        lex_outputfile='tc/for.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_expr(self):
        lex_outputfile='tc/expr.txt'
        self.assertEqual('accept', parse.parsefile(lex_outputfile))

    def test_panic(self):
        lex_outputfile='tc/panic1.txt'
        self.assertEqual('panic', parse.parsefile(lex_outputfile)) 



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
    unittest.TextTestRunner(verbosity=2).run(suite)