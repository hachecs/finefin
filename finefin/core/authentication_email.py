# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import User

class EmailAuthBackend:
    def authenticate(self,email=None,password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None 

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
