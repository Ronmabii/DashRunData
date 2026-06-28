import dash
from dash import Dash, html, dcc

app = Dash(__name__,use_pages=True) # gotta run from here always

app.layout = html.Div(
    [
        html.H1("Running Data"),
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

