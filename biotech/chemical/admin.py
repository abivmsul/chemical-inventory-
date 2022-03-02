from django.contrib import admin
from chemical.models import Chemical,RequestChemical, Request
# Register your models here.

admin.site.register(Chemical)
admin.site.register(RequestChemical)
admin.site.register(Request)
