import secrets
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm
from users.models import User
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404, redirect


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение электронной почты",
            message=f"Пожалуйста, подтвердите вашу электронную почту,"
                    f" перейдя по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
