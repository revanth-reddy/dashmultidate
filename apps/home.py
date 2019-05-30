import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import psycopg2
from datetime import datetime as dt
import dash_bootstrap_components as dbc

from app import app

app.css.append_css({
    "external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css",
    "external_url": "https://codepen.io/revanth-reddy/pen/bymxpZ.css"
})

conn = psycopg2.connect(host="john.db.elephantsql.com",database="hibzxjxl", user="hibzxjxl", password="BbJmB-QJQegz1z8f4jmsfsUY0GsNXehi")

cur = conn.cursor()
cur.execute("SELECT * from timetrend")
# print("The number of parts: ", cur.rowcount)
row = cur.fetchone()
time=[]
cov=[]
while row is not None:
            # print(row)
            time.append(row[0])
            cov.append(row[1])
            row = cur.fetchone()
# print(n)
cur.close()

dtmin = min(time)
dtmax = max(time)
# html.Div(dcc.Link(html.H3('Home'),style={'text-decoration': 'none'}, href = '/'),className='d-flex justify-content-center'),


layout = html.Div([
    dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Home Title", className="ml-2")),
                    dbc.Col(dbc.NavLink("link 1", href="/link1")),
                    dbc.Col(dbc.NavLink("link 2", href="/link2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
        color="dark",
        dark=True,
    ),
    dbc.Row(
        dbc.Col(
            dcc.Graph(id = 'livegraph', style={'width':'100%',}),
            width={"size": 6, "offset": 3},
        )
    ),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    ),
    html.Div(
    dcc.DatePickerRange(
        id='date-picker-range',
        display_format='MMM Do, YY ',
        min_date_allowed=dtmin,
        max_date_allowed=dt.now().date(),
        initial_visible_month=dt.now().date(),
        start_date = dtmin.date(),
        end_date = dtmax.date(),
    ),className='d-flex justify-content-center'),
    
    
    html.Div([
        dcc.Link('Go to Link 1', href='/link1'),
        html.Br(),
        dcc.Link('Go to Link 2', href='/link2'),
    ],className='d-flex justify-content-center'),
    
])


@app.callback(
    dash.dependencies.Output('livegraph', 'figure'),
    [dash.dependencies.Input('date-picker-range', 'start_date'),
     dash.dependencies.Input('date-picker-range', 'end_date')])
def graph_update_on_range(start_date,end_date):
    end_date = dt.strptime(end_date, "%Y-%m-%d").date()
    start_date = dt.strptime(start_date, "%Y-%m-%d").date()
    conn = psycopg2.connect(host="john.db.elephantsql.com",database="hibzxjxl", user="hibzxjxl", password="BbJmB-QJQegz1z8f4jmsfsUY0GsNXehi")

    cur = conn.cursor()
    cur.execute("SELECT * from timetrend")
    # print("The number of parts: ", cur.rowcount)
    row = cur.fetchone()
    time=[]
    cov=[]
    while row is not None:
                # print(row)
                date = row[0].date()
                
                if date <= end_date and date >= start_date:
                    time.append(row[0])
                    cov.append(row[1])
                row = cur.fetchone()
    
    cur.close()
    fig = go.Figure(
        data = [go.Scatter(
        x = time,
        y = cov,
        mode='lines',
        )],
    
    )
    return fig
