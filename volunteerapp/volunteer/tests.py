import json
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from volunteer.models import Organization  # , Event, Shift, Task
from users.models import Users


class OrganizationTestCase(APITestCase):

    def setUp(self):  # noqa
        """
        Set up test user and a sample organization
        for testing the duplicate error message
        """
        Users.objects.create_user(
            username='john',
            last_name='John',
            first_name='Crane',
            email='john@gmail.com',
            password='123'
        )
        Organization.objects.create(
            name='Duplicate Test Organization',
            description='Duplicate Description',
        )

    def test_create_organization_witout_auth(self):
        """
        Test the status code if a unauthenticated POST
        request is submitted
        """
        url = reverse('organization-list')
        data = {
            'name': 'Test Organization',
            'description': 'Test Description',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_organization_logged_in(self):
        """
        Test the status code and returned dataif an
        authenticated POST request is submitted
        """
        self.client.login(username='john', password='123')
        url = reverse('organization-list')
        data = {
            'name': 'Test Organization',
            'description': 'Test Description',
        }
        response_data = {
            'description': 'Test Description',
            'get_num_events': 0,
            'get_status_display': 'Draft Mode',
            'id': 3,
            'location': None,
            'name': 'Test Organization',
            'slug': 'test-organization',
            'status': 'DR'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(json.dumps(response.data), json.dumps(response_data))
        self.client.logout()

    def test_create_duplicate_organization(self):
        """
        Test the status code if an
        authenticated POST, but duplicated object
        is submitted
        """
        self.client.login(username='john', password='123')
        url = reverse('organization-list')
        data = {
            'name': 'Duplicate Test Organization',
            'description': 'Duplicate Description',
        }
        response_data = {u'name': [u'This field must be unique.']}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(json.dumps(response.data), json.dumps(response_data))
        self.client.logout()
