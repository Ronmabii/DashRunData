import dash
from dash import html, register_page
import dash_ag_grid as dag
import pandas as pd
from pathlib import Path

dash.register_page(__name__)

project_root = Path(__file__).parents[2] # folder organization vs csv path name
csvPath = project_root/ 'data'/'MILEAGE.csv'

df = pd.read_csv(csvPath)
df['Date'] = pd.to_datetime(df['Date']).dt.date # sort fix (repeats preventable?) tried new formatting but it turns into an unsortable object

layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field":"Date"}, {"field":"Activity Type"}, {"field":"Miles"}, {"field":"Duration(Mins)", "headerName": "Time"}, {"field":"Average Pace"}
                        , {"field":"Average Heart Rate"}, {"field":"Average Run Cadence"}, {"field":"Average Stride Length"} ],
            columnSize="autoSize",
            style={"width": "100%", "height": "80vh"}
            
        )
    ]
)