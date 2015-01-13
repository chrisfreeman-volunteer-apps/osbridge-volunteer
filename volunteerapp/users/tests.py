from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="john")
        User.objects.create(username="martha")

    def test_user(self):
        """Small test method"""
        john = User.objects.get(username="john")
        martha = User.objects.get(username="martha")
        self.assertEqual(john.username, 'john')
        self.assertEqual(martha.username, 'martha')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
