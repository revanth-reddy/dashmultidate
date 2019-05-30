import dash

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.append_css({
    "external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css",
    "external_url": "https://codepen.io/revanth-reddy/pen/bymxpZ.css"
})
server = app.server
app.config.suppress_callback_exceptions = True