import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from apps import app1, app2, home



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


server = server

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/link1':
        return app1.layout
    elif pathname == '/link2':
        return app2.layout
    else:
        return home.layout

# if __name__ == '__main__':
#     app.run_server()