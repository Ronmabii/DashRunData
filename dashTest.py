from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd


app = Dash()

df = pd.read_csv("TOTAL MILAGE Samsung + Nike + Garming up to May 2x, 2026 - Data.csv")

# app.layout = [html.Div(children="Heckoff",id="training-calendar-container")]

app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field":i} for i in df.columns]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)

# from dash import Dash, html, Input, Output, callback, ctx

# app = Dash()

# app.layout = html.Div(
#     [
#         html.Button("Button 1", id="btn-1"),
#         html.Button("Button 2", id="btn-2"),
#         html.Div(id="output-div"),
#     ]
# )


# @callback(
#     Output("output-div", "children"),
#     [
#         Input("btn-1", "n_clicks"),
#         Input("btn-2", "n_clicks"),
#     ],
# )
# def func(n_clicks_btn1, n_clicks_btn2):
#     button_id = ctx.triggered_id
#     message = f"You've clicked {button_id} last" if button_id else "No clicks yet"
#     return message


# if __name__ == "__main__":
#     app.run(debug=True)