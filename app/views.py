from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import SignUpForm


class Home(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(TemplateView):
    template_name = "signin/register.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        # Process the form submission
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully! Please log in."
            )
            return redirect("login")

        return render(request, self.template_name, {"form": form})


class UserLoginView(TemplateView):
    template_name = "signin/login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_password = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully!!")
                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

        return render(request, self.template_name, {"form": form})
