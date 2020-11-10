from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    """get_todo_list:

    Return the todo list to the template

    \n Args:
    1.  request: A user entered http request in the address bar

    \n Returns:
    1. the todo_list.html template.
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """add_item:

    Return the add_item template

    \n Args:
    1.  request: A user entered http request in the address bar

    \n Returns:
    1. the add_item.html template.
    """

    return render(request, 'todo/add_item.html')
