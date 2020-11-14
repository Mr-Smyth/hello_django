from django import forms  # this will allow us to use django form functionality
from .models import Item

# our form will be a class that inherits a built in django class
# To give it some basic functionality


# Create a class to inherit all the forms.ModelForm functionality
class ItemForm(forms.ModelForm):
    class Meta:
        """Meta

        Tells the form which model it is associated with
        this gives our form some information about itself

        """
        # tell it to use the item model
        model = Item
        # Which fields it should display from the model
        fields = ['name', 'done']
