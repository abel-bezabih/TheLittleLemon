from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import MenuItem, Booking
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.utils import timezone

class MenuItemTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.item = MenuItem.objects.create(title="Burger", price=10.00, inventory=100)
    
    def test_menu_item_str(self):
        """Test the string representation of MenuItem"""
        self.assertEqual(str(self.item), "Burger : 10.00")  # Ensure 2 decimal places for price

class MenuItemViewTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu_item = MenuItem.objects.create(title="Burger", price=10.00, inventory=100)

    def test_get_all_items(self):
        """Test GET request for all menu items"""
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_item(self):
        """Test POST request to create a new menu item"""
        data = {'title': 'Pizza', 'price': 15.00, 'inventory': 50}
        response = self.client.post('/api/menu-items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_item(self):
        """Test PUT request to update an existing menu item"""
        data = {'title': 'Updated Burger', 'price': 12.00, 'inventory': 80}
        response = self.client.put(f'/api/menu-items/{self.menu_item.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        """Test DELETE request to delete a menu item"""
        response = self.client.delete(f'/api/menu-items/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BookingTest(TestCase):
    def setUp(self):
        # Use timezone.now() to get the current datetime
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=timezone.now()  # Ensure it's a datetime object
        )

    def test_booking_str(self):
        # Test the string representation of the booking
        self.assertEqual(str(self.booking), "John Doe - 4 guests on " + self.booking.booking_date.strftime("%Y-%m-%d"))

class BookingViewTest(TestCase):
    def setUp(self):
        """Set up test data for bookings"""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.booking = Booking.objects.create(name="John Doe", no_of_guests=4, booking_date="2025-02-25")

    def test_get_all_bookings(self):
        """Test GET request for all bookings"""
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_booking(self):
        """Test POST request to create a new booking"""
        data = {'name': 'Jane Doe', 'no_of_guests': 2, 'booking_date': '2025-02-26'}
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_booking(self):
        """Test PUT request to update an existing booking"""
        data = {'name': 'Updated Name', 'no_of_guests': 5, 'booking_date': '2025-02-27'}
        response = self.client.put(f'/api/bookings/{self.booking.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_booking(self):
        """Test DELETE request to delete a booking"""
        response = self.client.delete(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
