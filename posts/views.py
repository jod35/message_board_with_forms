from django.views.generic import TemplateView,ListView


class HomePageView(TemplateView):
    template_name="posts/index.html"

class AddPostView(TemplateView):
    template_name="posts/add.html"

class LoginView(TemplateView):
    template_name="posts/login.html"

class SignUpView(TemplateView):
    template_name="posts/signup.html"