import django_filters 

from .models import *

class DriversFilter(django_filters.FilterSet):
    class Meta:
        model = Drivers
        fields = '__all__'
    