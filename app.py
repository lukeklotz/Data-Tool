#import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
#import dash
#from dash import dcc, html, Input, Output, callback

import os
from revenueData import *
from buildCostChart import *
#from utils import *

app = dash.Dash(__name__)

#this is necessary for deployment on render
server = app.server

#load data
costData = costData()
revData = revenueData()

displayCostGraph(app, costData, revData)

update_cost_graph(app)
update_revenue_graph(app)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) #use for render hosting
    #app.run_server(debug=True) #use for local development
