
from django.db import models

# Create your models here.
from taxi import globalTrainResults

class Taxi(models.Model):
    id=models.AutoField(primary_key=True)
    idTaxi = models.CharField(default=0, null=False, max_length=50)
    dropoff_latitude =  models.FloatField(default=0, null=False)
    dropoff_longitude =  models.FloatField(default=0, null=False)
    passenger_count =  models.IntegerField(default=0, null=False)
    pickup_latitude =  models.FloatField(default=0, null=False)
    pickup_longitude =  models.FloatField(default=0, null=False)
    hour_of_day =  models.IntegerField(default=0, null=False)
    day_of_week =  models.IntegerField(default=0, null=False)
    day_of_year =  models.IntegerField(default=0, null=False)
    year =  models.IntegerField(default=0, null=False)
    eucl_distance =  models.FloatField(default=0, null=False)
    manh_distance =  models.FloatField(default=0, null=False)
    fare_amount = models.FloatField(null=True)
    estimated_fare = models.FloatField(null=True)


    def save_estimate(self):
        # Get variables and model
        model = globalTrainResults['model']
        variables = globalTrainResults['variables']
        # Prepare data: must be in the same order as the model was trained


        data = [self.__dict__[var_name] for var_name in variables]
        # Use model to predict
        self.estimated_fare = model.predict([data])
        self.save()

    class Meta:
        unique_together = ('idTaxi',)