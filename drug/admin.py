from django.contrib import admin
from .models import Drug_detail, Drug_category, Emchilgee, History
# Register your models here.

admin.site.register(Drug_category)
admin.site.register(Drug_detail)
admin.site.register(Emchilgee)
admin.site.register(History)
