from django.contrib import admin
from .models import Degree, Gender, Position, User, Worker, Costumer
# Register your models here.

admin.site.register(Gender)
admin.site.register(Position)
admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Costumer)
admin.site.register(Degree)
