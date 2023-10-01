from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache


class SunCircumferenceViewTest(TestCase):
    def setUp(self):
        # Add a dummy pi value to cache for testing
        cache.set("pi_value", "3.14")

    def test_view_url_exists(self):
        response = self.client.get(reverse("sun_circumference"))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_data(self):
        response = self.client.get(reverse("sun_circumference"))
        self.assertEqual(response.data["pi_value"], "3.14")
        self.assertTrue("circumference" in response.data)

    def test_view_no_pi_in_cache(self):
        cache.delete("pi_value")
        response = self.client.get(reverse("sun_circumference"))
        self.assertEqual(response.status_code, 404)
