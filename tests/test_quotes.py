import unittest
from app.models import  Quote


class quoteTest(unittest.TestCase):
    '''
    Quotes test case to check the behavior of the quote class
    '''

    def setup(self):
        '''
        A method that runs before any other test runs
        '''

        self.new_quote=Quote("16", "Yogi Berra", "In theory, theory and practice are the same. In practice, they’re not.", "http://quotes.stormconsultancy.co.uk/quotes/16")
    
    def test_init(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

if __name__=='__main__':
    unittest.main()
    