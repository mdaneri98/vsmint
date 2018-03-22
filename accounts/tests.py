# Create your tests here.
from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from .forms import *   # import all forms
from .models import UserProfile


class User_Form_Test(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = 'mdaneri98', 
            password = 'Ezequiel',
            email = 'mdaneri98@gmail.com',
            first_name = 'Matias',
            last_name = 'Daneri'
        )


    #Test's the profile creation.
    def test_profile_creation(self):
        profile = UserProfile.objects.get(user = self.user)
        self.assertEqual(profile.user_id, self.user.pk)

    #Test the profile creation on a form.
    def test_profile_creation_by_form(self):
        profile_form = ProfileForm({
            'username': 'matidaneri',
            'password1': 'Ezequiel',
            'password2': 'Ezequiel',
            'email': 'mdaneri88@gmail.com',
            'description': 'Mine it is.'
        })
        profile_form.full_clean()
        profile_form.save()
        user = User.objects.get(username='matidaneri')
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.user, user)
            

    #Just to see if the user was saved properly.        
    def test_user_creation(self):
        self.assertEqual(self.user.email, 'mdaneri98@gmail.com')


    # Valid Form Data
    def test_UserForm_valid(self):
        form = ProfileForm({
            'email': "mdaneri98@gmail.com", 
            'username': "mdaneri12",
            'first_name': 'matias',
            'last_name': 'daneri',
            'password1': 'EzequiEl',
            'password2': 'EzequiEl',
            'description': 'asds'
            })
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    # Invalid password-mismatch Form Data
    def test_UserForm_mismatch_invalid(self):
        form = ProfileForm({
            'email': "mdaneri98@gmail.com", 
            'username': "mdaneri12",
            'first_name': 'matias',
            'last_name': 'daneri',
            'password1': 'ezequieel',
            'password2': 'mismatchpassword',
            'description': 'asds'
            })
        is_valid = form.is_valid()
        self.assertFalse(form.is_valid())

     # Invalid password-no-upperCase Form Data
    def test_UserForm_uppercase_invalid(self):
        form = ProfileForm({
            'email': "mdaneri98@gmail.com", 
            'username': "mdaneri12",
            'first_name': 'matias',
            'last_name': 'daneri',
            'password1': 'ezequieel',
            'password2': 'ezequieel',
            'description': 'asds'
            })
        self.assertFalse(form.is_valid())


  