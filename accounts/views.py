from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from . import forms as accounts_forms
from django.views.generic import FormView


class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = accounts_forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("posts:home")

    
def log_out(request):
    logout(request) 
    return redirect(reverse("posts:home"))


def SignupView(request):
    if request.method == "GET":
        form = accounts_forms.SignupForm()
        return render(request, "accounts/signup.html", {"form": form})

    if request.method == "POST":
        form = accounts_forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  
                return redirect(reverse("posts:home"))
        return render(request,"accounts/signup.html",{"form":form})
        
