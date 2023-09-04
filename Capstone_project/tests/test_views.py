from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title = 'Pasta', price = 20, inventory = 78)
        Menu.objects.create(title = 'Sushi', price = 100, inventory = 88)

    def test_getall(self):
        all_items = Menu.objects.all()
        self.assertEqual(str(all_items), '<QuerySet [<Menu: Pasta : 20.00>, <Menu: Sushi : 100.00>]>')