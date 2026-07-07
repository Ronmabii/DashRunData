import dash
from dash import html
import dash_ag_grid as dag
import pandas as pd
from pathlib import Path

dash.register_page(__name__)

project_root = Path(__file__).parents[2]
csvPath = project_root/ 'data'/'Races.csv'

df = pd.read_csv(csvPath)
df['Date'] = pd.to_datetime(df['Date']).dt.date

layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns ],
            defaultColDef={"cellRenderer":"markdown"}, # allows hyperlinks
            columnSize="autoSize"
            
        )
    ]
)