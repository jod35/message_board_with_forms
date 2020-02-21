from django.views.generic import TemplateView,ListView


class HomePageView(TemplateView):
    template_name="index.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class LoginView(TemplateView):
    template_name="login.html"

class SignUpView(TemplateView):
    template_name="signup.html"