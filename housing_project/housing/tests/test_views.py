from django.test import TestCase

from django.contrib.auth.models import User

from housing.models import Location

from accounts.models import UserProfile


class HousingViewTest(TestCase):

    def setUp(self):

        self.location = Location.objects.create(
            name='Darwin',
            region='NT'
        )

        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        UserProfile.objects.create(
            user=self.user,
            role='USER',
            community_name='Test Community',
            contact_number='123456789'
        )


    def test_login_required_for_create_page(self):

        response = self.client.get('/create/')

        self.assertEqual(
            response.status_code,
            302
        )


    def test_normal_user_cannot_create_housing(self):

        self.client.login(
            username='testuser',
            password='password123'
        )

        response = self.client.get('/create/')

        self.assertEqual(
            response.status_code,
            403
        )