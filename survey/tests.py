# Create your tests here.
from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from .forms import *   # import all forms
from .models import UserProfile


class Survey_Test(TestCase):

    def setUp(self):
        user = User(
            username = 'mdaneri18', 
            password = 'Ezequiel',
            email = 'mdaneri98@gmail.com',
            first_name = 'Matias',
            last_name = 'Daneri'
        )
        user.save()


    