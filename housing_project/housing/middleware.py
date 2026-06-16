from django.shortcuts import render

from housing.exceptions import (
    InvalidHousingPriceError,
    HousingNotAvailableError,
    UnauthorizedActionError
)


class GlobalExceptionMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)

        return response


    def process_exception(self, request, exception):

        if isinstance(
            exception,
            InvalidHousingPriceError
        ):

            return render(
                request,
                'errors/price_error.html',
                {
                    'error': str(exception)
                },
                status=400
            )

        if isinstance(
            exception,
            HousingNotAvailableError
        ):

            return render(
                request,
                'errors/not_found.html',
                {
                    'error': str(exception)
                },
                status=404
            )

        if isinstance(
            exception,
            UnauthorizedActionError
        ):

            return render(
                request,
                'errors/unauthorized.html',
                {
                    'error': str(exception)
                },
                status=403
            )

        return render(
            request,
            'errors/general_error.html',
            {
                'error': str(exception)
            },
            status=500
        )