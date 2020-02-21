from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView
from .models import Post,User

class HomePageView(TemplateView):
    template_name="posts/index.html"

class AddPostView(CreateView):
    model=Post
    template_name="posts/add.html"
    fields='__all__'

class LoginView(TemplateView):
    template_name="posts/login.html"

class SignUpView(TemplateView):
    template_name="posts/signup.html"