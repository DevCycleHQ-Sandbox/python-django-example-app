from django.http import HttpResponse, JsonResponse
import logging
import datetime
import time

from devcycle_python_sdk.models.user import DevCycleUser

logger = logging.getLogger("views")

variable_key = "test-boolean-variable"


def home_page(request):
    start = time.time_ns()
    # all functions require user data to be an instance of the User class

    user = DevCycleUser(
        user_id="test",
        email="example@example.ca",
        country="CA",
    )
    # Check whether a feature flag is on
    if request.devcycle.variable_value(user, variable_key, False):
        time_end = time.time_ns()
        time_taken = time_end - start
        logger.warning(f"view eval time ns: {time_taken} ")
        return JsonResponse({"msg": "Hello, World! Your feature is on!", "time_for_eval_ns": time_taken})
    else:
        logger.info(f"{variable_key} is off")
        return HttpResponse("Hello, World! Your feature is off.")


def admin_page(request):
    start = time.time_ns()
    # all functions require user data to be an instance of the User class

    user = DevCycleUser(
        user_id="admin",
        email="example@example.ca",
        country="CA",
    )
    # Check whether a feature flag is on
    if request.devcycle.variable_value(user, "admin", False):
        time_end = time.time_ns()
        time_taken = time_end - start
        logger.warning(f"view eval time ns: {time_taken} ")
        return JsonResponse({"msg": "Hello, Admin! Your feature is on!", "time_for_eval_ns": time_taken})
    else:
        logger.info(f"{variable_key} is off")
        return HttpResponse("Hello, Admin! Your feature is off.")

def maintenance_page(request):
    start = time.time_ns()
    # all functions require user data to be an instance of the User class

    user = DevCycleUser(
        user_id="maintenance",
        email="example@example.ca",
        country="CA",
    )
    # Check whether a feature flag is on
    if request.devcycle.variable_value(user, "maintenance", False):
        time_end = time.time_ns()
        time_taken = time_end - start
        logger.warning(f"view eval time ns: {time_taken} ")
        return JsonResponse({"msg": "Hello, This is Maintenance! Your feature is on!", "time_for_eval_ns": time_taken})
    else:
        logger.info(f"{variable_key} is off")
        return HttpResponse("Hello, This is Maintenance! Your feature is off.")
