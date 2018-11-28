from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseModelBackend

User = get_user_model()


class EmailLoginBackend(BaseModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is not None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
