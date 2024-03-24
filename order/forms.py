from . models import Order
from django import forms

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =  ['first_name', 'last_name', 'email',  'phone_no', 'address',
                    'city']