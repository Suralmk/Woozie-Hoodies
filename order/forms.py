from . models import Order
from django import forms

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =  ['first_name', 'last_name', 'email',  'phone_no', 'address',
                    'city']
    
    def __init__(self, *args, **kwargs):
        super(CreateOrderForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['phone_no'].widget.attrs['placeholder'] = '+2519...'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter your address'
        self.fields['city'].widget.attrs['placeholder'] = 'Enter your city'