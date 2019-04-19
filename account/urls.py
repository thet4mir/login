from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    url(r'^worker-list/$',views.WorkerList.as_view(), name="worker-list"),
    url(r'^costumer-list/$',views.CostumerList.as_view(), name="costumer-list"),
    url(r'^worker/$',views.WorkerCreate.as_view(),name='worker_create'),
    url(r'^costumer/$',views.CostumerCreate.as_view(),name='costumer_create'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
]
