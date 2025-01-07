from django import forms
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone', 'address', 'date_of_birth', 'city']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

from django import forms
from .models import CareerForm

class CareerFormModel(forms.ModelForm):
    class Meta:
        model = CareerForm
        fields = '__all__'  # Include all fields in the model

    # Custom validation for user_id can be done in the view, not directly in the form
    def save(self, commit=True):
        # Ensure that the logged-in user is set for the form
        career_form = super().save(commit=False)
        
        # Assign the current logged-in user to the form instance
        if self.instance.user is None:
            career_form.user = self.user  # Assuming `self.user` is passed in the view
        
        if commit:
            career_form.save()
        return career_form


from django import forms
from .models import Widget

class WidgetForm(forms.ModelForm):
    class Meta:
        model = Widget
        fields = ['title', 'content', 'elfsight_embed_code']



