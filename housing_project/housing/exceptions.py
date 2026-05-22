class HousingError(Exception):
    pass


class InvalidHousingPriceError(HousingError):
    pass


class HousingNotAvailableError(HousingError):
    pass


class UnauthorizedActionError(HousingError):
    pass