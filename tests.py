import unittest
import parse

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

    '''def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            '''

if __name__ == '__main__':
    unittest.main()