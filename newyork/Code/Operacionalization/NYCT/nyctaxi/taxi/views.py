from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from taxi.models import *
from taxi.serializers import *
from taxi import dashboard

import pandas as pd
from nyctaxi.settings import TAXI_MODEL_WORKDIR


# Create your views here.

def dashboard_home(requests):
    dashboard.update_dash()
    return render(requests, 'taxi/welcome.html')

class TaxiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Taxi to be viewed or edited.
    """
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

class TaxiAPIView(APIView):
    """
    API endpoint that allows Taxi to be viewed or edited.
    """
    def get(self, request):
        serializer = TaxiSerializer(Taxi.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        data = dict([(k,float(v[0]) if isinstance(v, list) else (v))
                     for k,v in request.data.items()
                    ])

        taxi, created = Taxi.objects.get_or_create(**data)
        if created:
            taxi.save_estimate()

        serializer = TaxiSerializer(taxi, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

class getDatabase(APIView):
  """
  """
  def get(self, request):
      # Read database from pipeline_training
      data_proc_file = TAXI_MODEL_WORKDIR + '/Data/Modeling/dev_results.jbl'
      data = pd.read_parquet(data_proc_file)
      data = data.copy()

      taxi_list = []
      for irow, row in data.iterrows():
          
          if not Taxi.objects.filter(idTaxi=row.idTaxi).exists():
            taxis = Taxi(idTaxi=row.idTaxi,
                                    dropoff_latitude =  row.dropoff_latitude,
                                    dropoff_longitude =  row.dropoff_longitude,
                                    passenger_count =  row.passenger_count,
                                    pickup_latitude =  row.pickup_latitude,
                                    pickup_longitude =  row.pickup_longitude,
                                    hour_of_day =  row.hour_of_day,
                                    day_of_week =  row.day_of_week,
                                    day_of_year =  row.day_of_year,
                                    year =  row.year,
                                    eucl_distance =  row.eucl_distance,
                                    manh_distance =  row.manh_distance,
                                    fare_amount = row.fare_amount,
                                    estimated_fare = row.estimated_fare)
            taxi_list.append(taxis)
          


      # Bulk insert
      if len(taxi_list):
          Taxi.objects.bulk_create(taxi_list)
    
      #Taxi.save_estimate(data)

      serializer = TaxiSerializer(Taxi.objects.all(), many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

