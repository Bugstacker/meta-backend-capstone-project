from django.test import TestCase
from .models import Menu

# Create your tests here.


class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="test", price=10, inventory=10)

        self.assertEqual(item.__str__(), 'test : 10')

    def test_get_all(self):
        Menu.objects.create(title="test", price=10, inventory=10)
        Menu.objects.create(title="test2", price=10, inventory=10)
        Menu.objects.create(title="test3", price=10, inventory=10)

        self.assertEqual(Menu.objects.all().count(), 3)
