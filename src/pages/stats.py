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
        dbc.Card(# pie chart bike/run/elip?
            html.Div(
                html.H4(
                    "Runs : " + str(df.shape[0])
                ),className=f" border-start border-5"
            ),className="text-center text-nowrap my-2 p-2",style={"width": "20rem"} 
        ),

        dbc.Card( 
                    html.Div(
                        html.H4(
                            "Miles Ran : " + str(df["Miles"].sum()) + "miles"
                        ),className=f" border-start border-5"
                    ),className="text-center text-nowrap my-2 p-2",style={"width": "20rem"} 
                ),

        dbc.Card( # bar chart max average min run heart rate
            html.Div(
                html.H4(
                    "Max Heart Rate : 203 bpm"
                ),className=f" border-start border-5"
            ),className="text-center text-nowrap my-2 p-2",style={"width": "20rem"} 
        ),

        dbc.Card(
                    html.Div( # chart weight range 155 to 132
                        html.H4(
                            "Weight : 132 lb"
                        ),className=f" border-start border-5"
                    ),className="text-center text-nowrap my-2 p-2",style={"width": "20rem"} 
                ) 
        ]
         
    ) 
)