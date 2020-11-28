from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.pastword

class Prediction(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    patinte_id = models.CharField(max_length=100, null=True, blank=True)
    patiente_age = models.CharField(max_length=100, null=True, blank=True)
    analysis_date = models.CharField(max_length=100, null=True, blank=True)
    prediction = models.CharField(max_length=100, null=True, blank=True)
    eeg = models.CharField(max_length=100, null=True, blank=True)
    process = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Prediction'

class LoadDataProces(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    patinte_id = models.CharField(max_length=100, null=True, blank=True)
    patiente_age = models.CharField(max_length=100, null=True, blank=True)
    analysis_date = models.CharField(max_length=100, null=True, blank=True)
    prediction = models.CharField(max_length=100, null=True, blank=True)
    eeg = models.CharField(max_length=100, null=True, blank=True)
    process = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'LoadDataProces'

class Plot(models.Model):
    edfName = models.CharField(max_length=100, null=True, blank=True)
    count = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Plot'
   



























