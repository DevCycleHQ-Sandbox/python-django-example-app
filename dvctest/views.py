from django.http import HttpResponse

from devcycle_python_sdk import Configuration, DVCClient, UserData
from devcycle_python_sdk.rest import ApiException

configuration = Configuration()
configuration.api_key['Authorization'] = '<YOUR DEVCYCLE SERVER SDK KEY>'
dvc = DVCClient(configuration)

# # all functions require user data to be an instance of the UserData class
user = UserData(
    user_id='test',
    email='example@example.ca',
    country='CA'
)

def homePageView(request):
    try:
        # Get all features by key for user data
        variable = dvc.variable(user, 'test', 'default-value')
        print("Variable value is: ", variable.value)
        if variable.value:
            return HttpResponse("Hello, World! true")
        else:
            return HttpResponse("Hello, World! false")
    except ApiException as e:
        print("Exception when calling DVCClient->all_features: %s\n" % e)
        return HttpResponse("broken")

    