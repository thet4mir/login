from django.contrib import admin
from .models import Drug_detail, Drug_category, Emchilgee, History, Onosh, Drug_important, Drug_order
# Register your models here.

admin.site.register(Drug_category)
admin.site.register(Drug_important)
admin.site.register(Drug_order)
admin.site.register(History)
admin.site.register(Onosh)
