import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


app = Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.SUPERHERO]) # must run from app.py
server = app.server

app.layout = html.Div(
    [
        html.H1("2026 NYC Marathon Training Data 🏃"),
        html.Div([
                dcc.Link(page['name']+ "  |  ", href=page['path'])
                for page in dash.page_registry.values()
            ]),
        html.Hr(),

        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run(debug=True)