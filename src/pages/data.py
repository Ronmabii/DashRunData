import dash
from dash import html, register_page
import dash_ag_grid as dag
import pandas as pd
from pathlib import Path

dash.register_page(__name__)

csvPath = Path(__file__).parent.parent.parent/'data'/'Mileage.csv'

df = pd.read_csv(csvPath)

layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field":"Date"}, {"field":"Miles"} ]
        )
    ]
)