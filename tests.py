from app import app
import unittest

class TestViews(unittest.TestCase):

    def test_shopping_list(self):
        tester = app.test_client(self)
        response = tester.get('/shopping_list', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Items' in response.data)

    
    def test_get_items(self):
        tester = app.test_client(self)
        response = tester.get('/get_items', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Supplies' in response.data)


    def test_add_category(self):
        tester = app.test_client(self)
        response = tester.get('/add_category', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_edit_category(self):
        tester = app.test_client(self)
        response = tester.get('/editcategory', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_search_results(self):
        tester = app.test_client(self)
        response = tester.get('/search_results', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_add_item(self):
        tester = app.test_client(self)
        response = tester.get('/additem', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_edit_item(self):
        tester = app.test_client(self)
        response = tester.get('/edititem', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
  unittest.main()