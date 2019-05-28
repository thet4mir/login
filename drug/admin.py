from django.contrib import admin
from .models import Days_of_emchilgee, Drug_detail, Drug_category, Emchilgee, History, Onosh, Drug_important, Drug_order, Doctor_review, Emchilgee_list
# Register your models here.

admin.site.register(Drug_detail)
admin.site.register(Drug_category)
admin.site.register(Doctor_review)
admin.site.register(Days_of_emchilgee)
admin.site.register(History)
admin.site.register(Emchilgee_list)
