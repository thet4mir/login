from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    url(r'^singup/$',views.WorkerCreate,name='worker_create'),
]
