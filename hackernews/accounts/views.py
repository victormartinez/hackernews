from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from hackernews.accounts.forms import UserLoginForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        if form.cleaned_data['keep_signed']:
            self.request.session.set_expiry(604800)  # 1 week
        else:
            self.request.session.set_expiry(0)
        return super(UserLoginView, self).form_valid(form)
