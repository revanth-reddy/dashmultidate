import dash

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [
    "https://codepen.io/revanth-reddy/pen/bymxpZ.css",
    "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css",
    ]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


server = app.server
app.config.suppress_callback_exceptions = True