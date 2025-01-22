from barGraph import *

def displayMaterials(app):

    app.layout = html.Div(
    className="materials-parent",  # Applying the "parent" class from CSS
    children=[
        html.H1("hello", className="h1"),
        html.Div("Box 1", className="box"),
        html.Div("Box 2", className="box"),
        html.Div("Box 3", className="box"),
    ]
)