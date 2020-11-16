from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_new_item_is_not_done(self):
        item = Item.objects.create(name='Test Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # Create a new test item
        item = Item.objects.create(name='Test Item')
        # Then use assertEqual to check if this name is returned
        # when we render this item as a string
        self.assertEqual(str(item), 'Test Item')
