from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    url(r'^list/$',views.WorkerList.as_view(), name="list"),
    url(r'^singup/$',views.WorkerCreate.as_view(),name='worker_create'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
]
