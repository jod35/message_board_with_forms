from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomePageView.as_view(),name="site_home"),
    path("about/",views.AddPostView.as_view(),name='site_about'),
    path("login/",views.LoginView.as_view(),name="site_login"),
    path("signup/",views.SignUpView.as_view(),name="site_signup"),
    path("add/",views.AddPostView.as_view(),name='posts/add.html')
]