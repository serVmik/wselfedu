from http import HTTPStatus

from django.test import Client, TestCase


class HomePageTest(TestCase):
    """Test home page view."""

    def setUp(self):
        """Set suite up."""
        self.client = Client()

    def test_home_page_view(self):
        """Test home page 200 status."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('WSE', str(response.content))
