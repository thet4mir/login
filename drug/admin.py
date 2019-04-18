from django.contrib import admin
from .models import Drug_detail, Drug_category
# Register your models here.

admin.site.register(Drug_category)
admin.site.register(Drug_detail)
