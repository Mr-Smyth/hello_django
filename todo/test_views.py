from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    # Test we can get the home page
    def test_get_todo_list(self):
        # use built in http client to get the response code
        response = self.client.get('/')
        # does respose = 200
        self.assertEqual(response.status_code, 200)
        # check if correct template is returned by the view
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # Test get the add item page
    def test_get_add_item_page(self):
        # use built in http client to get the response code
        response = self.client.get('/add')
        # does respose = 200
        self.assertEqual(response.status_code, 200)
        # check if correct template is returned by the view
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # Test getting the edit item page
    def test_get_edit_item_page(self):
        # create a mock item to use in our test
        item = Item.objects.create(name='Test_item')
        # use built in http client to get the response code
        response = self.client.get(f'/edit/{item.id}')
        # does respose = 200
        self.assertEqual(response.status_code, 200)
        # check if correct template is returned by the view
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # Test that we can add an item
    def test_can_add_item(self):
        # create a response equal to adding a test item
        response = self.client.post('/add', {'name': 'Test Item'})
        # check if the response causes redirect back to home page
        self.assertRedirects(response, '/')

    # Test that we can delete an item
    def test_can_delete_item(self):
        # create a mock item to use in our test
        item = Item.objects.create(name='Test_item')
        # pass the id into the delete view
        response = self.client.get(f'/delete/{item.id}')
        # check if the response causes redirect back to home page
        self.assertRedirects(response, '/')
        # Search for the deleted item to see if its length is now 0
        existing_item = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_item), 0)

    # Test can we toggle an item
    def test_can_toggle_item(self):
        # create a mock item to use in our test and add a done status
        item = Item.objects.create(name='Test_item', done=True)
        # pass in the id to the toggle view
        response = self.client.get(f'/toggle/{item.id}')
        # check if the response causes redirect back to home page
        self.assertRedirects(response, '/')
        # Get the item again
        updated_item = Item.objects.get(id=item.id)
        # check that its done status has been changed
        self.assertFalse(updated_item.done)
