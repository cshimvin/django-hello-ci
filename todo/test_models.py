from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # Create a test item
        item = Item.objects.create(name="Test Todo Item")
        # Check that done is set to false by default
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # Create a a test item
        item = Item.objects.create(name="Test Todo Item")
        # Check that the string item returns the name
        self.assertEqual(str(item), 'Test Todo Item')
