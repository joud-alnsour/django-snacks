from django.test import TestCase
from django.urls import resolve
from .views import HomePageView

class HomePageViewViewTest(TestCase):
    def test_resolve_to_home_page_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.__name__, HomePageView.as_view().__name__)

    def test_home_page_status_code_is_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)