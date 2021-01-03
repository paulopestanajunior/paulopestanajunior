import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py
import datetime
from django_plotly_dash import DjangoDash
from plotly.subplots import make_subplots
from taxi import models
from taxi import serializers
import plotly.figure_factory as ff

import numpy as np
import math
from random import sample

from nyctaxi.settings import TAXI_MODEL_WORKDIR
from taxi import globalTrainResults



dev_data = TAXI_MODEL_WORKDIR + '/Data/Modeling/dev_results.jbl'
prev_data = TAXI_MODEL_WORKDIR + '/Data/Processed/nyctaxi_data_analysis_green.parquet'

# Training data
data = pd.read_parquet(dev_data)

#PRediction New Data
data_prev = pd.read_parquet(prev_data)
data_prev['idTaxi'] =  data_prev['pickup_latitude'].astype(str)+'_'+data_prev['pickup_longitude'].astype(str)+'_'+data_prev['day_of_year'].astype(str)+'_'+data_prev['year'].astype(str)
data_prev['estimated_fare'] = 0

# Read operation data
# ALERTA: COMENTAR ANTES DE FAZER python manage.py migrate.
# DESCOMENTAR DEPOIS PARA FUNCIONAR CORRETAMENTE
taxi_list = models.Taxi.objects.order_by('-estimated_fare')
taxi_data = serializers.TaxiSerializer(taxi_list, many=True)
taxi_table = pd.DataFrame(taxi_data.data)
model = globalTrainResults['model']


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            val = row[i] if isinstance(row[i],str) else '%.2f'%(row[i])
            html_row.append(html.Td([val]))
        table.append(html.Tr(html_row))
    return table



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] #['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash(
    "TaxiDashboard",
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    # external_stylesheets=external_stylesheets
)

def update_dash():
    # Create dist plots
    hist_data = [taxi_table['fare_amount'].values, taxi_table['estimated_fare'].values]
    fig_dist = ff.create_distplot(hist_data, ['Preço Real', 'Preço Estimado'],show_hist=False)
    ntop = 10

    model = globalTrainResults['model']
    variables = globalTrainResults['variables']

    df_feature_importances = pd.DataFrame(model.feature_importances_*100,columns=["Importance"],index=variables)
    df_feature_importances = df_feature_importances.sort_values("Importance", ascending=False)

    # We create a Features Importance Bar Chart
    fig_features_importance = go.Figure()
    fig_features_importance.add_trace(go.Bar(x=df_feature_importances.index,
                                            y=df_feature_importances["Importance"],
                                            marker_color='rgb(171, 226, 251)')
                                    )
    fig_features_importance.update_layout(title_text='<b>Features Importance<b>', title_x=0.5)


    yearly_analysis  = taxi_table.groupby("year").agg({"idTaxi":"count",
                                                 "fare_amount":"sum",
                                                 "passenger_count":"sum",
                                                 "eucl_distance" : "sum"}).reset_index()
    #aggregating by year
    yearly_analysis = yearly_analysis.rename(columns = {"idTaxi" : "trip_count"})

    #plotting trips ,passengers and fare amount by year
    def plotting(column) : 
        tracer = go.Bar(x= yearly_analysis["year"],y = yearly_analysis[column],
                        marker = dict(line = dict(width = 1)),
                        name = column
                    )
        return tracer

    #layout
    layout1 = go.Layout(dict(title = "Total  trips ,passengers,trip_distance and fare amount by year",
                            plot_bgcolor  = "rgb(243,243,243)",
                            paper_bgcolor = "rgb(243,243,243)",
                            xaxis = dict(gridcolor = 'rgb(255, 255, 255)',title = "year",
                                        zerolinewidth=1,ticklen=5,gridwidth=2),
                            yaxis = dict(gridcolor = 'rgb(255, 255, 255)',title = "count",
                                        zerolinewidth=1,ticklen=5,gridwidth=2),
                        )
                    )
        
    data = [plotting("trip_count"),plotting("passenger_count"),
            plotting("eucl_distance"),plotting("fare_amount")]
    fig1  = go.Figure(data=data,layout=layout1)

    trips_hr = taxi_table["hour_of_day"].value_counts().reset_index()
    trips_hr.columns = ["hour_of_day","count"]
    trips_hr = trips_hr.sort_values(by = "hour_of_day",ascending = True)

    trace = go.Scatter(x = trips_hr["hour_of_day"],y = trips_hr["count"],
                    mode = "markers+lines",
                    marker = dict(color = "red",size = 9,
                                    line = dict(color = "black",width =2)))
    #layout
    layout2 = go.Layout(dict(title = "Trend in trips  by hour of day",
                            plot_bgcolor  = "rgb(243,243,243)",
                            paper_bgcolor = "rgb(243,243,243)",
                            xaxis = dict(gridcolor = 'rgb(255, 255, 255)',title = "hour_of_day",
                                        zerolinewidth=1,ticklen=5,gridwidth=2),
                            yaxis = dict(gridcolor = 'rgb(255, 255, 255)',title = "count",
                                        zerolinewidth=1,ticklen=5,gridwidth=2),
                        )
                    )

    fig2 = go.Figure(data = [trace],layout = layout2)

    avg_fare_hr = taxi_table.groupby("hour_of_day")["fare_amount"].mean().reset_index()
    avg_est_fare_hr = taxi_table.groupby("hour_of_day")["estimated_fare"].mean().reset_index()
    avg_fare_hr
    trace1 = go.Scatter(x = avg_fare_hr["hour_of_day"],y = avg_fare_hr["fare_amount"],
                    mode = "markers+lines",
                    marker = dict(color = "blue",size = 9,
                                    line = dict(color = "black",width =2)),
                    name = 'Valor Real')
    trace2 = go.Scatter(x = avg_est_fare_hr["hour_of_day"],y = avg_est_fare_hr["estimated_fare"],
                    mode = "markers+lines",
                    marker = dict(color = "red",size = 9,
                                    line = dict(color = "black",width =2)),
                    name = 'Valor Previsto')

    #layout
    layout3 = go.Layout(dict(title = "Average fare by hour",
                            plot_bgcolor  = "rgb(243,243,243)",
                            paper_bgcolor = "rgb(243,243,243)",
                            xaxis = dict(gridcolor = 'rgb(255, 255, 255)',title = "hour_of_day",
                                        zerolinewidth=1,ticklen=5,gridwidth=2),
                            yaxis = dict(gridcolor = 'rgb(255, 255, 255)',title = "average_fare",
                                        zerolinewidth=1,ticklen=5,gridwidth=2),
                        )
                    )

    fig3 = go.Figure(data = [trace1,trace2],layout = layout3 )

    app.layout = html.Div(children=[
        html.H1(children='Dashboard das Tarifas de Taxis na cidade de Nova York'),

        html.P(children='''
            Desenvolvimento de modelos de previsão de tarifas das corridas de táxi na cidade de Nova York
        '''),
        dcc.Graph(figure=fig_features_importance),

        html.Div([
            # New Div for both plots
            html.Div([
                html.Div([
                    dcc.Graph(figure=fig1),
                    dcc.Graph(figure=fig2),
                    dcc.Graph(figure=fig3),
                    
                ], className="six columns"),           

                html.Div([
                    html.H3('Maiores ' + str(ntop) + ' Tarifas'),
                    html.H4(['idTaxi ',' | fare_amount | ','  estimated_fare']),
                    html.Table(make_dash_table(taxi_table[['idTaxi','fare_amount','estimated_fare']].head(ntop)))
                ], className="six columns"),

                html.Div([
                    html.H3('Distribuição das Tarifas'),
                    dcc.Graph(
                        id='score-dist',
                        figure=fig_dist
                    )
                ], className="six columns"),

                html.Div([
                    html.H3('Previsão'),
                    html.Button('Previsão', id='previsao'),
                    html.Div(id='output-container-button',
                            children=''),
                ], className="six columns"),

                html.Div([
                    html.H3('Maiores ' +  ' Tarifas'),
                    html.H5(['idTaxi ',' | fare_amount | ','  estimated_fare']),
                    html.Table(
                        children = '',
                        id='tabela',
                    ),
                ], className="six columns"),

            ], className="row")
        ]),
    ])

    

@app.callback(
    Output(component_id='output-container-button', component_property='children'),
    [Input(component_id='previsao', component_property='n_clicks')]
)
def previsao_botao(n_clicks):

    if n_clicks:
        result = model.predict([data_prev[globalTrainResults['variables']]][0])
        data_prev['estimated_fare'] = result
        result = "US $ "+ str(result[n_clicks-1])
        return result
    else:
        return "Aperte o botão para realizar uma previsão"
    
@app.callback(
    Output(component_id='tabela', component_property='children'),
    [Input(component_id='previsao', component_property='n_clicks')]
)
def update_tabela(n_clicks):
    if n_clicks:
        return make_dash_table(data_prev[['idTaxi','fare_amount','estimated_fare']].head(n_clicks))
    else:
        return make_dash_table(data_prev[['idTaxi','fare_amount','estimated_fare']].head(0))