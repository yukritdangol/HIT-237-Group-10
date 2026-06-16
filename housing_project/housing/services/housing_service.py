from housing.models import Housing
from housing.exceptions import (
    InvalidHousingPriceError,
    HousingNotAvailableError
)


class HousingService:

    @staticmethod
    def get_available_housing():

        return Housing.objects.filter(
            is_available=True
        ).order_by('price')


    @staticmethod
    def create_housing(
        title,
        location,
        price,
        description
    ):

        if price < 0:
            raise InvalidHousingPriceError(
                "Price cannot be negative."
            )

        housing = Housing.objects.create(
            title=title,
            location=location,
            price=price,
            description=description,
            is_available=True
        )

        return housing


    @staticmethod
    def mark_unavailable(housing_id):

        try:

            housing = Housing.objects.get(
                id=housing_id
            )

        except Housing.DoesNotExist:

            raise HousingNotAvailableError(
                "Housing does not exist."
            )

        housing.is_available = False

        housing.save()

        return housing