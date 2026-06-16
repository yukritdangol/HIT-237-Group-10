from django.test import TestCase

from housing.models import (
    Housing,
    Location
)

from housing.services.housing_service import (
    HousingService
)

from housing.exceptions import (
    InvalidHousingPriceError
)


class HousingServiceTest(TestCase):

    def setUp(self):

        self.location = Location.objects.create(
            name='Darwin',
            region='NT'
        )


    def test_create_housing_success(self):

        housing = HousingService.create_housing(
            title='Service House',
            location=self.location,
            price=600,
            description='Service Description'
        )

        self.assertEqual(
            housing.title,
            'Service House'
        )

        self.assertEqual(
            housing.price,
            600
        )


    def test_negative_price_exception(self):

        with self.assertRaises(
            InvalidHousingPriceError
        ):

            HousingService.create_housing(
                title='Bad House',
                location=self.location,
                price=-100,
                description='Invalid'
            )