from django.test import TestCase
# Import the Item model from models.py so we can test dabatase functionality
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        # Get the URL from Django URLs
        response = self.client.get('/')
        # Check the status code is OK (i.e. OK)
        self.assertEqual(response.status_code, 200)
        # Check the page template displayed is correct
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Create an item to test the response
        item = Item.objects.create(name="Test Todo Item")
        # Use string literal to get the correct URL based on the item.id
        # created in the database
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # Simulate submitting the Add Item form with data
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Check that the Add Item page redirects to homepage when
        # form is subbmited via POST method
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # Create an item to be deleted
        item = Item.objects.create(name="Test Todo Item")
        # Use string literal to get the correct URL based on the item.id
        # created in the database
        response = self.client.get(f'/delete/{item.id}')
        # Check that the Delete Item page redirects to homepage when
        # form is subbmited via POST method
        self.assertRedirects(response, '/')
        # Check item deleted from database by getting the item ID
        # then checking the length to confirm it is 0 (i.e. deleted)
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Create an item to be toggled
        item = Item.objects.create(name="Test Todo Item", done=True)
        # Use string literal to get the correct URL based on the item.id
        # created in the database
        response = self.client.get(f'/toggle/{item.id}')
        # Check that the Toggle Item page redirects to homepage when
        # form is subbmited via POST method
        self.assertRedirects(response, '/')
        # Check the item's done status has been updated to False
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        # Create an item to test the response
        item = Item.objects.create(name="Test Todo Item")
        # Use string literal to get the correct URL based on the item.id
        # created in the database and update the name to test edit works
        response = self.client.post(f'/edit/{item.id}',
                                    {'name': 'Updated Name'})
        # Test application reqdirects to homepage once edited
        self.assertRedirects(response, '/')
        # Check item updated in database
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
