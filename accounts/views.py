from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from .forms import registerForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.views import View
from django.shortcuts import redirect

from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

# password change
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView


class registerViewModel(FormView):
    template_name = 'accounts/user_registration.html' 
    form_class = registerForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('signIn')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('signIn')

class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
        return render(request, self.template_name, {'form': form})
    

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/passwordchange.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'your password has been changed'
        )

        mail_subject = 'password change'
        message =f'your password has been changed'
        to_email = self.request.user.email 
        send_email  = EmailMultiAlternatives(mail_subject, '', to=[to_email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()

        return response