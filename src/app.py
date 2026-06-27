from dash import Dash, html, dcc, callback, Output,Input,ctx
import pandas as pd
from pathlib import Path
import plotly.express as px


app = Dash()

csvPath = Path(__file__).parent.parent/'data'/'Mileage.csv'

df = pd.read_csv(csvPath)

df[["Date","Week (Monday)"]] = df[["Date","Week (Monday)"]].apply(pd.to_datetime) # needs this to be recognized as a continuous timeline, otherwise compressed(str to datetime)

weeklyMileageSum = (
    df.groupby("Week (Monday)", as_index=False)["Miles"] # dff["Miles"].sum() without as_index wrong column entered into fig
      .sum()
)

app.layout = html.Div(
    [
        html.H1("Running Data"),
        html.Button("Overall", id="btn-overall"),
        html.Button("Weekly", id="btn-week"),
        dcc.Graph(id="chart", figure = {}, style={"width": "100%", "height": "80vh"})
    ]
)

@callback(
    Output("chart", "figure"),
    [
        Input("btn-overall", "n_clicks"),
        Input("btn-week", "n_clicks"),
    ],
)
def func(n_clicks_btn1, n_clicks_btn2):
    button_id = ctx.triggered_id

    if button_id == "btn-week":
        fig = px.bar(weeklyMileageSum, x="Week (Monday)",y="Miles",labels={"Week (Monday)": "Weeks"},title="Weekly Running Mileage")
    else:
        fig = px.scatter(df,x='Date',y='Miles',title="Running Timeline")

    return fig


if __name__ == '__main__':
    app.run(debug=True)

