from django import forms

class contactUsForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': "form-control"}))