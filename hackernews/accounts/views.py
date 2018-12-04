from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse_lazy
from django.views.generic import CreateView

from hackernews.accounts.forms import UserLoginForm, UserSignUpForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        if form.cleaned_data['keep_signed']:
            self.request.session.set_expiry(604800)  # 1 week
        else:
            self.request.session.set_expiry(0)
        return super(UserLoginView, self).form_valid(form)


class UserSignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        messages.success(self.request, 'Your account was created. Please, login.')
        return super(UserSignUpView, self).form_valid(form)

    def get_success_url(self):
        self._send_welcome_mail()
        return super().get_success_url()

    def _send_welcome_mail(self):
        user = self.object
        html_content = render_to_string('mailing/welcome.html', {'user': user})
        text_content = strip_tags(html_content)

        message = EmailMultiAlternatives(
            subject='[Hackernews] Welcome {}'.format(user.first_name),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
            body=text_content
        )

        message.attach_alternative(html_content, "text/html")
        message.send(fail_silently=True)
