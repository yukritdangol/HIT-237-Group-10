from django.test import TestCase

from housing.models import (
    Housing,
    Location
)


class HousingModelTest(TestCase):

    def setUp(self):

        self.location = Location.objects.create(
            name='Darwin',
            region='NT'
        )

        self.housing = Housing.objects.create(
            title='Test Housing',
            location=self.location,
            price=500,
            description='Test Description',
            is_available=True
        )


    def test_housing_creation(self):

        self.assertEqual(
            self.housing.title,
            'Test Housing'
        )

        self.assertEqual(
            self.housing.price,
            500
        )

        self.assertTrue(
            self.housing.is_available
        )


    def test_location_string(self):

        self.assertEqual(
            str(self.location),
            'Darwin'
        )


    def test_housing_string(self):

        self.assertEqual(
            str(self.housing),
            'Test Housing'
        )