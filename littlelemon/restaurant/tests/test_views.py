from django.test import TestCase
from ..models import Menu
from rest_framework.test import APIClient
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        """Setup test data."""
        # Create a few Menu objects for testing
        self.menu_item_1 = Menu.objects.create(title="Burger", price=150, inventory=50)
        self.menu_item_2 = Menu.objects.create(title="Pizza", price=200, inventory=30)
        self.menu_item_3 = Menu.objects.create(title="Pasta", price=100, inventory=70)
        
        # Set up the API client for making requests
        self.client = APIClient()
        self.url = "/api/menu/"
    def test_getall(self):
        response = self.client.get(self.url)
        expected_data = MenuSerializer([self.menu_item_1, self.menu_item_2, self.menu_item_3], many=True).data
        self.assertEqual(response.data,expected_data)