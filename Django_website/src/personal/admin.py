from django.contrib import admin
from .models import Question,Drivers,Results,Circuits,Constructor,Races

# Register your models here.

admin.site.register(Question)
admin.site.register(Drivers)
admin.site.register(Results)
admin.site.register(Circuits)
admin.site.register(Constructor)
admin.site.register(Races)