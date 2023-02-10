import unittest
import product_database as pdb

class TestGroceryQueries(unittest.TestCase):

    def test_categories(self):
        self.assertEqual(len(pdb.get_product_categories()), 6)

    def test_categories(self):
        self.assertEqual(len(pdb.get_products("Fruits")), 5)
    
    def test_create_user(self):
        #Unique so I cannot make duplicates
        with self.assertRaises(Exception):
            pdb.create_user('yoel@gmail.com', 'Yoel', '12345')
    
    


if (__name__ == '__main__'):
    unittest.main()