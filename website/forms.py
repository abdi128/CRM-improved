from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control mt-1','placeholder':''}), label="Email")
    first_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control mt-1','placeholder':''}), label="First Name:")
    last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control mt-1','placeholder':''}), label="Last Name:")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control mt-1'
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control mt-1'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control mt-1'
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = ''	



class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="First Name")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="Last Name")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="Email")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="Phone")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="Address")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="City")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-3 mt-1"}), label="State")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control mb-4 mt-1"}), label="Zip Code")

	class Meta:
		model = Record
		exclude = ("user",)