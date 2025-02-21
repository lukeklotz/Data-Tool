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
data = Data()

coverGlass = data.getCoverGlass()
backContact = data.getBackContact() 
absorber = data.getAbsorber() 
etl = data.getEtl() 

costData = Data()
revData = revenueData()

#drop down and background styles
width            = '70%'
dd_color         = '#353431'
bg_color         = '#23221B'
background_color = '#8E9FA3'

#bar graph styles
font_color  = "#afa732"
font_family = "Courier New"

displayCostGraph(app, costData, revData)

update_cost_graph(app)
update_revenue_graph(app)

# Run the app
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) #use for render hosting
    app.run_server(debug=True) #use for local development
