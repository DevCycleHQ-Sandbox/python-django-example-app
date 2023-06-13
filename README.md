# DevCycle Python Django Example App

Welcome to the the DevCycle Python Django Example App, for sample usage with the [DevCycle Python Server SDK](https://github.com/DevCycleHQ/python-server-sdk).
To find Python SDK usage documentation, visit our [docs](https://docs.devcycle.com/docs/sdk/server-side-sdks/python#usage).

## Requirements.

Python 3.4+ and Django 4.2+

## Installation

```sh
pip install -r requirements.txt
```
(you may need to run `pip` with root permission: `sudo pip install -r requirements.txt`)

## Usage

To run the example app:
```sh
python manage.py migrate
python manage.py runserver
```

See [settings.py](https://github.com/DevCycleHQ/python-django-example-app/blob/main/config/settings.py#L132) for the
singleton instantiation of the `DVCClient()` object, and [views.py](https://github.com/DevCycleHQ/python-django-example-app/blob/main/dvctest/views.py#L8)
for an example of its usage.

*Please note that instantiating the `DVCClient()` object in the Django settings file is not considered a best practice
for Django, but is a temporary accommodation due to some conflicts between thread pool handling in the DevCycle SDK and
Django management commands. Scheduled work on the DevCycle Python SDK revisits how the thread pool is handled, and ensures
more graceful cleanup and closing of threads so that SDK users do not need to take that into consideration.* 