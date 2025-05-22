from rest_framework.views import exception_handler
import sentry_sdk


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None and response.status_code != 500:
        sentry_sdk.capture_exception(exc)
    return response
