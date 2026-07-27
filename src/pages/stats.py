import dash
from dash import html
import dash_ag_grid as dag
import pandas as pd
from pathlib import Path
import dash_bootstrap_components as dbc

dash.register_page(__name__)

project_root = Path(__file__).parents[2]
csvPath = project_root/ 'data'/'MILEAGE.csv'

df = pd.read_csv(csvPath)
df['Date'] = pd.to_datetime(df['Date']).dt.date

# loop the repeats / add max speed races
layout = html.Div(
    dbc.Stack(
        [
        dbc.Card(
            html.Div(
                html.H4(
                    "Runs : " + str(df.shape[0])
                ),className=f" border-start border-5"
            ),className="text-center text-nowrap my-2 p-2"
        ),

        dbc.Card(
            html.Div(
                html.H4(
                    "Max Heart Rate : 203 bpm (Garmin watch heart rate sensor)"
                ),className=f" border-start border-5"
            ),className="text-center text-nowrap my-2 p-2"
        ),

        dbc.Card(
                    html.Div(
                        html.H4(
                            "Weight : 132 lb"
                        ),className=f" border-start border-5"
                    ),className="text-center text-nowrap my-2 p-2"
                ) 
        ]
        ,style={"width": "18rem"}  
    ) 
)