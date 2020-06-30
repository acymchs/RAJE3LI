from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class DetailViewTests(TestCase):
    def test_lesson_detail(self):
        response=self.client.get(reserve('courses:lesson_detail')
        self.assertEqual(response.status_code,200)
