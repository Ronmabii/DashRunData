import dash
from dash import html, register_page
import dash_ag_grid as dag
import pandas as pd
from pathlib import Path

dash.register_page(__name__)

PROJECT_ROOT = Path(__file__).parents[2] # folder organization vs csv path name
csvPath = PROJECT_ROOT/ 'data'/'Mileage.csv'

df = pd.read_csv(csvPath)

layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field":"Date"}, {"field":"Miles"} ]
        )
    ]
)