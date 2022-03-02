from django.contrib import admin
from account.models import Researcher,Custodian,Department,Director
# Register your models here.
admin.site.register(Researcher)
admin.site.register(Custodian)
admin.site.register(Director)
admin.site.register(Department)