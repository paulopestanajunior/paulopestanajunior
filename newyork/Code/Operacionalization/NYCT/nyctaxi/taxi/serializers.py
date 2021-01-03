
from rest_framework import serializers
from taxi import models


class TaxiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Taxi
        fields = ['idTaxi','dropoff_latitude','dropoff_longitude','passenger_count',
                  'pickup_latitude','pickup_longitude','hour_of_day',
                  'day_of_week','day_of_year','year','eucl_distance',
                  'manh_distance','fare_amount','estimated_fare']
    