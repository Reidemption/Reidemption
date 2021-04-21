"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import isbn_index

class test_listBooksAction( unittest.TestCase ):

    def input_replacement( self, prompt ):
        self.assertFalse( self.too_many_inputs )
        self.input_given_prompt = prompt
        r = self.input_response_list[ self.input_response_index ]
        self.input_response_index += 1
        if self.input_response_index >= len( self.input_response_list ):
            self.input_response_index = 0
            self.too_many_inputs = True
        return r

    def print_replacement( self, *text ):
        line = " ".join( text ) + "\n"
        self.printed_lines.append( line )
        return
    
    def setUp(self):
        
        self.too_many_inputs = False
        self.input_given_prompt = None
        self.input_response_index = 0
        self.input_response_list = [ "" ]
        isbn_index.input = self.input_replacement

        self.printed_lines = [ ]
        isbn_index.print = self.print_replacement

        
        return

    def tearDown(self):
        return
    
    def test001_listBooksActionExists(self):
        self.assertTrue('listBooksAction' in dir( isbn_index ),
                        'Function "listBooksAction" is not defined, check your spelling')
        return
    
    def test002_listBooksActionListsBooks(self):
        isbn1 = "0000-00000000"
        title1 = "Book Title"
        isbn2 = "0000-12345678"
        title2 = "War of the Worlds"
        index = { isbn1: title1, isbn2: title2 }
        expected = { isbn1: title1, isbn2: title2 }

        self.input_response_list = [ "???" ]
        isbn_index.listBooksAction( index )
        self.assertDictEqual( index, expected )
        
        self.assertGreaterEqual( len( self.printed_lines ), 2 )

        printed_text = "".join( self.printed_lines )
        self.assertIn( isbn1, printed_text )
        self.assertIn( title1, printed_text )
        self.assertIn( isbn2, printed_text )
        self.assertIn( title2, printed_text )
        return

if __name__ == '__main__':
    unittest.main()
