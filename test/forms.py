from django import forms
from .models import House, Manush, Search
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Manush
        fields = ('name', 'username', 'phone', 'pic', 'gender', 'occupation', 'dob')

        labels = {
            'dob': 'Date of Birth (YYYY-MM-DD)',
            'profile_img': 'Profile Picture'
        }

    def __init__(self, *args, **kwargs) -> None:
        super(RegistrationForm, self).__init__(*args, **kwargs)

        class_attr = 'form-control'
        self.fields['name'].widget.attrs['class'] = class_attr
        self.fields['username'].widget.attrs['class'] = class_attr
        self.fields['password1'].widget.attrs['class'] = class_attr
        self.fields['password2'].widget.attrs['class'] = class_attr
        self.fields['phone'].widget.attrs['class'] = class_attr
        self.fields['pic'].widget.attrs['class'] = class_attr
        self.fields['gender'].widget.attrs['class'] = class_attr
        self.fields['occupation'].widget.attrs['class'] = class_attr
        self.fields['dob'].widget.attrs['class'] = class_attr

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('details', 'price','location' ,'gender', 'pic','rent_date', 'bedroom_no','bathroom_no','flat_size','type')
        flat_type = forms.MultipleChoiceField(choices=House.TYPE_CHOICES)
        class_attr = 'form-control'
        labels = {
            'price': 'Rent',
            'rent_date': 'Available From',
            'flat_size': 'Flat/Room size'          
        }
        widgets = {
            'details': forms.Textarea(attrs={'class': class_attr}),
            'loaction' : forms.TextInput(attrs={'class': class_attr}),
            'price': forms.NumberInput(attrs={'class': class_attr}),
            'pic': forms.ClearableFileInput(attrs={'class': class_attr}),
            'gender': forms.TextInput(attrs={'class': class_attr}),
            'rent_date': forms.DateInput(format='%Y-%m-%d'),
            'bedroom_no': forms.NumberInput(attrs={'class': class_attr}), 
            'bathroom_no' : forms.NumberInput(attrs={'class': class_attr}),
            'flat_size' : forms.NumberInput(attrs={'class': class_attr}),
            
        }

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('location', 'price1', 'price2', 'gender','type')
        flat_type = forms.MultipleChoiceField(choices=House.TYPE_CHOICES)
        class_attr = 'form-control'
        labels = {
            'price1': 'Minimum Rent',
            'price2': 'Maximum Rent'
        }

        widgets = {
            'loaction' : forms.TextInput(attrs={'class': class_attr}),
            'price1': forms.NumberInput(attrs={'class': class_attr}),
            'price2': forms.NumberInput(attrs={'class': class_attr}),
            'gender': forms.TextInput(attrs={'class': class_attr}),
        }