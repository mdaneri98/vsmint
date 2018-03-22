from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class ProfileForm(forms.ModelForm):

    password1 = forms.CharField(
        max_length = 30,
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Must have a capital letter."
        )

    password2 = forms.CharField(
        max_length = 30,
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
        ps1 = cleaned_data.get('password1')
        ps2 = cleaned_data.get('password2')
        if ps1 != ps2:
            raise forms.ValidationError(
                "Passwords must match!",
                code = "password_mismatch"
                ) 
        return cleaned_data#Es el nuevo cleaned_data del form. Por eso hay que devolverlo

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()  # User obtiene primaryKey y se crea el ProfileUser

        profile = UserProfile.objects.get(user = user)
        profile.description = self.cleaned_data["description"]
        if commit:
            profile.save()

        return user