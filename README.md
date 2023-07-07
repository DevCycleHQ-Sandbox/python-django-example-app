# DevCycle Python Django Example App

Welcome to the the DevCycle Python Django Example App, for sample usage with the [DevCycle Python Server SDK](https://github.com/DevCycleHQ/python-server-sdk).
To find Python SDK usage documentation, visit our [docs](https://docs.devcycle.com/docs/sdk/server-side-sdks/python#usage).

## Requirements.

Python 3.7+ and Django 4.2+

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

See [settings.py](https://github.com/DevCycleHQ/python-django-example-app/blob/main/config/settings.py#L135) for the
the configuration of your SDK key in the `DEVCYCLE_SERVER_SDK_KEY` setting, and [views.py](https://github.com/DevCycleHQ/python-django-example-app/blob/main/devcycle_test/views.py) for an example of using the DevCycle client to check the value of a feature flag.

For convenience, a middleware implementation is used to add the DevCycle client to the request object, so you can access it in your views as `request.devcycle`. See `middleware.py` for details. There are two examples of middleware, one for each type of DevCycle SDK: cloud bucketing and local bucketing.
