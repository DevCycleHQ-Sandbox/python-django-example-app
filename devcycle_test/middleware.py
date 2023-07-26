from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from devcycle_python_sdk import (
    DevCycleCloudClient,
    DevCycleCloudOptions,
    DevCycleLocalClient,
    DevCycleLocalOptions,
)
from django.shortcuts import redirect
from devcycle_python_sdk.models.user import DevCycleUser
import logging
import time


logger = logging.getLogger("middleware")


class MaintenanceModeMiddleware:
    """This middleware is used to put the site into maintenance mode.

    This must be after the devcycle middleware as it depends on it.

    The maintenace_allow_list is a list of paths that are allowed to be accessed
    it was sourced from what used to exist in urls.py but hasn't been vetted.
    the /admin panel does not allow access to admin as currently designed.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time_ns()
        path = request.META.get("PATH_INFO", "")
        if request.devcycle.variable_value(
            user=DevCycleUser(user_id="maintenance"),
            key="maintenance",
            default_value=False,
        ):
            time_end = time.time_ns()
            logger.warning(f"DOWN_FOR_MAINTENANCE: {path} redirecting to /maintenance")
            logger.warning(f"middleware eval time ns: {time_end - start} ")
            maintenance_allow_list = [
                "/admin/",
                "/health",
                "/maintenance",
            ]

            for allowed_path in maintenance_allow_list:
                if path.startswith(allowed_path):
                    return self.get_response(request)
            return redirect("/maintenance")
        if path.startswith(
            "/maintenance"
        ):  # if we're on the maintenance page and not down for maintenance, redirect to /
            return redirect("/")
        time_end = time.time_ns()
        logger.warning(f"middleware eval time ns: {time_end - start} ")

        return self.get_response(request)


def devcycle_cloud_middleware(get_response):
    """
    This middleware adds the DevCycle client to the request object passed to
    all views as `request.devcycle`.
    """
    try:
        sdk_key = settings.DEVCYCLE_SERVER_SDK_KEY
    except AttributeError:
        raise ImproperlyConfigured("Please set DEVCYCLE_SERVER_SDK_KEY in settings.py")

    # Initialize the SDK singleton once here - it will be captured in the closure below
    devcycle_client = DevCycleCloudClient(sdk_key, DevCycleCloudOptions())

    def middleware(request):
        request.devcycle = devcycle_client
        return get_response(request)

    return middleware


def devcycle_local_middleware(get_response):
    """
    This middleware adds the DevCycle client to the request object passed to
    all views as `request.devcycle`.
    """
    try:
        sdk_key = settings.DEVCYCLE_SERVER_SDK_KEY
    except AttributeError:
        raise ImproperlyConfigured("Please set DEVCYCLE_SERVER_SDK_KEY in settings.py")

    # Initialize the SDK singleton once here - it will be captured in the closure below
    devcycle_client = DevCycleLocalClient(sdk_key, DevCycleLocalOptions())

    def middleware(request):
        request.devcycle = devcycle_client
        return get_response(request)

    return middleware
