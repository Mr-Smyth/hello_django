from django.shortcuts import render, HttpResponse


# Create your views here.

def say_hello(request):
    """say_hello:

    * Simple function that take an Http request from the user
    and returns a http response.
    * We need to add this function into our
    urls.py so that it is available to the web browser.

    \n Args:
    1.  request: A user entered http request in the address bar

    Returns:
    1. A http response, saying Hello.
    """
    return HttpResponse("Hello!")
