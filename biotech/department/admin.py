from django.contrib import admin
from department.models import *
# Register your models here.

admin.site.register(AnimalStore)
admin.site.register(PlantStore)
admin.site.register(MicrobialStore)
admin.site.register(AnimalDesposedChemical)
admin.site.register(PlantDesposedChemical)
admin.site.register(MicrobialDesposedChemical)
 