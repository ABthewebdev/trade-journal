from django.contrib import admin
from .models import Trade, Enter_Trade, Exit_Trade

# Register your models here.
admin.site.register(Trade)
admin.site.register(Exit_Trade)
admin.site.register(Enter_Trade)