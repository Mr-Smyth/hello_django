from django.shortcuts import render


# Create your views here.

def get_todo_list(request):
    """get_todo_list:

    \n Args:
    1.  request: A user entered http request in the address bar

    \n Returns:
    1. the todo_list.html template.
    """
    return render(request, 'todo/todo_list.html')
