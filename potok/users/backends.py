from django.contrib.auth.backends import BaseBackend
from .models import Doctor, Expert
from django.contrib.auth.models import User


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Expert.objects.get(email=email)
        except Expert.DoesNotExist:
            try:
                user = Doctor.objects.get(email=email)
            except Doctor.DoesNotExist:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    return None

        if user.check_password(password):
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return Expert.objects.get(pk=user_id)
        except Expert.DoesNotExist:
            try:
                return Doctor.objects.get(pk=user_id)
            except Doctor.DoesNotExist:
                try:
                    return User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    return None
