from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


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

    * Return the add_item template
    * Gets new task from template and posts to DB

    \n Args:
    1.  request: A user entered http request in the address bar

    \n Returns:
    1. the add_item.html template.
    2. in POST: returns get_todo_list
    """
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    """edit_item:

    * Get and update a todo item
    * Return the edit_item template

    \n Args:
    1.  request: A user entered http request in the address bar
    2.  item_id: The id of the item clicked, and is attached to each edit
        button.

    \n Returns:
    1. the edit_item.html template.
    """
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    """toggle_item:

    * Toggle the items done status

    \n Args:
    1.  request: A user entered http request in the address bar
    2.  item_id: The id of the item clicked, and is attached to each toggle
        button.

    \n Returns:
    1. the todo_list.html template.
    """
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')
 

def delete_item(request, item_id):
    """delete_item:

    * delete the chosen item.

    \n Args:
    1.  request: A user entered http request in the address bar
    2.  item_id: The id of the item clicked, and is attached to each delete
        button.

    \n Returns:
    1. the todo_list.html template.
    """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
