from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile


'''
Every time a user is created, also a profile related to that user is created.
'''
def user_created(sender, **kwargs):
    if kwargs['created']:
        user_instance = kwargs['instance']
        UserProfile.objects.create(user= user_instance)
        


#Conects the User post_save to user_created
post_save.connect(user_created,sender= User)