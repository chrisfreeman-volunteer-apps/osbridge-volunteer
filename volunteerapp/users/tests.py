from django.test import TestCase
from users.models import Users


class UserTestCase(TestCase):
    def setUp(self):  # noqa
        Users.objects.create(username="john")
        Users.objects.create(username="martha")

    def test_user(self):
        """Small test method"""
        john = Users.objects.get(username="john")
        martha = Users.objects.get(username="martha")
        self.assertEqual(john.username, 'john')
        self.assertEqual(martha.username, 'martha')
