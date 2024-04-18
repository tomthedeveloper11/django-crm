from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("customers/<int:id>", views.customer_records, name="customers"),
    path("add_record/", views.add_record, name="add_record"),
]
