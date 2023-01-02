from django.db import models

# Create your models here.

PRIORITY = [
    ("L","Low"),
    ("M","Medium"),
    ("H","High")
    
]

class Question(models.Model):
    title                   = models.CharField(max_length = 60)
    question                = models.TextField(max_length = 400)
    priority                = models.CharField(max_length = 1,choices =PRIORITY)
    
    
    def __str__(self): # if we print the object, this is what will appear
        return self.title

    class Meta :
        verbose_name = "The Question"
        verbose_name_plural = "Peoples Questions"
    


class Drivers(models.Model):
    driverid = models.FloatField(primary_key=True)
    driverref = models.CharField(max_length=20, blank=True, null=True)
    forename = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'


class Circuits(models.Model):
    circuitid = models.FloatField(primary_key=True)
    circuitref = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    lat = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    alt = models.BigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuits'


class Constructor(models.Model):
    constructorid = models.FloatField()
    constructorref = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'constructor'
        

class Races(models.Model):
    raceid = models.FloatField(primary_key=True)
    round = models.FloatField(blank=True, null=True)
    circuitid = models.ForeignKey(Circuits, models.DO_NOTHING, db_column='circuitid')
    name = models.CharField(max_length=40, blank=True, null=True)
    datetime_field = models.DateField(db_column='datetime_', blank=True, null=True)  # Field renamed because it ended with '_'.
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'races'
        


class Results(models.Model):
    resultid = models.FloatField(primary_key=True)
    raceid = models.FloatField(blank=True, null=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driverid', blank=True, null=True)
    constructorid = models.FloatField(blank=True, null=True)
    num_car = models.FloatField(blank=True, null=True)
    start_pos = models.BigIntegerField(blank=True, null=True)
    final_pos = models.BigIntegerField(blank=True, null=True)
    positiontext = models.CharField(max_length=20, blank=True, null=True)
    positionorder = models.CharField(max_length=20, blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    nbr_laps = models.BigIntegerField(blank=True, null=True)
    time_total = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    num_fastestlap = models.FloatField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    fastestlaptime = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    fastestlapspeed = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'
        
        

