import dash
from dash import html, dcc, callback, Output,Input,ctx, register_page
import pandas as pd
from pathlib import Path
import plotly.express as px

dash.register_page(__name__,path='/') # Home Page

PROJECT_ROOT = Path(__file__).parents[2] # folder organization vs csv path name
csvPath = PROJECT_ROOT/ 'data'/'MILEAGE.csv' # files name caps matter more than you know
df = pd.read_csv(csvPath)

df[["Date","Week (Monday)"]] = df[["Date","Week (Monday)"]].apply(pd.to_datetime) # needs this to be recognized as a continuous timeline, otherwise compressed(str to datetime)
df['Duration(Mins)'] = pd.to_timedelta(df['Duration(Mins)']) 
df["Minutes"] = df["Duration(Mins)"].dt.total_seconds() /60# would be easier to convert to seconds in csv

weeklyMileageSum = (
    df.groupby("Week (Monday)", as_index=False)["Miles"] # dff["Miles"].sum() without as_index wrong column entered into fig
      .sum()
)

dffHR = df[df["Average Heart Rate"] > 120] # super low ones might be walks

layout = html.Div(
    [
        html.Button("Overall Mileage", id="btn-overall"),
        html.Button("Weekly Mileage", id="btn-week"),
        html.Button("Heart Rate", id="btn-heart"),
        html.Button("Time", id="btn-duration"),
        dcc.Graph(id="chart", figure = {}, style={"width": "100%", "height": "80vh"})
    ]
)

# callbacks run when page loaded
@callback(
    Output("chart", "figure"),
    [
        Input("btn-overall", "n_clicks"), 
        Input("btn-week", "n_clicks"),
        Input("btn-heart", "n_clicks"),
        Input("btn-duration", "n_clicks"),
    ],
)
def func(n_clicks_btn1, n_clicks_btn2,n_clicks_btn3,n_clicks_btn4):
    button_id = ctx.triggered_id

    if button_id == "btn-week":
        fig = px.bar(weeklyMileageSum, x="Week (Monday)",y="Miles",labels={"Week (Monday)": "Weeks"},title="Weekly Running Mileage")
    elif button_id == "btn-heart":
        fig = px.scatter(dffHR, x='Date', y = 'Average Heart Rate',color="Activity Type", title="Average Heart Rate tracked starting from September 2024")
    elif button_id == "btn-duration":
        fig = px.scatter(df, x='Date', y = 'Minutes', range_x=["2023-9-01", "2026-06-30"],title="Duration of runs starting from October 2023")
        fig.update_xaxes(dtick="M3")
    else:
        fig = px.scatter(df,x='Date',y='Miles',title="Complete Tracked Mileage", hover_data= {"Date": "|%B %d, %Y"})

    return fig