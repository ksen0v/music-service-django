from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        model = get_user_model()
        try:
            user = model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (model.DoesNotExist, model.MultipleObjectsReturned):
            return None
        
    def get_user(self, user_id):
        model = get_user_model()
        try:
            return model.objects.get(pk=user_id)
        except model.DoesNotExist:
            return None
