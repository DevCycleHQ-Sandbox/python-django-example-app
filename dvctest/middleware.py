from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from devcycle_python_sdk import DevCycleCloudClient, DevCycleCloudOptions

def devcycle_middleware(get_response):
    try:
        sdk_key = settings.DEVCYCLE_SDK_KEY
    except AttributeError:
        raise ImproperlyConfigured("Please set DEVCYCLE_SDK_KEY in settings.py")

    # Initialize the SDK singleton once here - it will be captured in the closure below
    devcycle_client = DevCycleCloudClient(sdk_key, DevCycleCloudOptions())

    def middleware(request):
        request.flags = devcycle_client
        return get_response(request)

    return middleware
