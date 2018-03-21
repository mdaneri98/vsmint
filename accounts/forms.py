from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class ProfileForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
        )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
        )

    description = forms.CharField(
        label="Description"
    )

    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'first_name',
            'last_name'
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not any([x.isupper() for x in password1]):
            raise forms.ValidationError(
                "Password must have at least one upper case letter.",
                code = "No upper case."
                )    
        return password1

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()#También self.cleaned_data
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError(
                "Passwords must match!",
                code = "password_mismatch"
                ) 
        return cleaned_data#Es el nuevo cleaned_data del form. Por eso hay que devolverlo

