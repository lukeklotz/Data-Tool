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
<<<<<<< HEAD
data = Data()

# group data
coverGlass = data.getCoverGlass()
backContact = data.getBackContact() 
absorber = data.getAbsorber() 
etl = data.getEtl() 
=======
costData = Data()
>>>>>>> 1b3524d1d217fbb31407e1f314c6ddbbeffefd3c

#drop down and background styles
width            = '70%'
dd_color         = '#353431'
bg_color         = '#23221B'
background_color = '#8E9FA3'

#bar graph styles
font_color  = "#afa732"
font_family = "Courier New"

<<<<<<< HEAD
displayMaterials(app)

#displays bargraph. 

displayBarGraph(app, coverGlass, backContact, absorber, etl, width, dd_color, font_color, bg_color)

@app.callback(
        Output('cost-bar-chart', 'figure'),
        [
            Input('coverGlass-dropdown', 'value'),
            Input('backContact-dropdown', 'value'),
            Input('Absorber-dropdown', 'value'),
            Input('etl-dropdown', 'value')
        ]
    )

def update_graph(coverGlass, backContact, absorber, etl):

    # Create the bar chart
    fig = go.Figure()

    coverGlass = data.getCoverGlass()
    backContact = data.getBackContact() 
    absorber = data.getAbsorber() 
    etl = data.getEtl() 

    bar_title_font_style = dict(size=12, color="black", family=font_family)

    fig.add_trace(go.Bar(
        x=["Cover Glass"],
        y=[coverGlass["Cost"].values[0]],
        name="Cover Glass",
        marker=dict(color='red',
                    line=dict(width=2, color="black")),      # color
        text=[f"${coverGlass["Cost"].values[0]}"],         # cost label $x.xx
        textposition="outside", 
        textfont=bar_title_font_style        # font style
    ))

    fig.add_trace(go.Bar(
        x=["Back Contact"],
        y=[backContact["Cost"].values[0]],
        name="Back Contact",
        marker=dict(color='orange',
                    line=dict(width=2, color="black")),                 # color
        text=[f"${backContact["Cost"].values[0]}"],                    # cost
        textposition="outside",  
        textfont=bar_title_font_style,                   # font style
    ))

    fig.add_trace(go.Bar(
        x=["Absorber"],
        y=[absorber["Cost"].values[0]],
        name="Absorber",
        marker=dict(color='lightblue',
                line=dict(width=2, color="black")),                 # color
        text=[f"${absorber["Cost"].values[0]}"],                       # cost
        textposition="outside", 
        textfont=bar_title_font_style,                   # font style
    ))

    fig.add_trace(go.Bar(
        x=["ETL"],
        y=[etl["Cost"].values[0]],
        name="ETL",
        marker=dict(color='yellow',
                    line=dict(width=2, color="black")),                  # color
        text=[f"${etl["Cost"].values[0]}"],                       # cost
        textposition="outside",                     
        textfont=bar_title_font_style               # font style
    ))

    fig.add_trace(go.Bar(
        x=["Total"],
        y=["formatted_total_cost"],
        name="Total Cost",
        marker=dict(color='darkgreen',
                    line=dict(width=2, color="black")),
        text=[f"$formatted_total_cost"],
        textposition="outside",
        textfont=bar_title_font_style,
    ))

     # Add annotation for the total cost
    fig.add_annotation(
        text=f"Total Cost: $formatted_total_cost",
        xref="paper", yref="paper",
        x=1.29, y=0.0,
        showarrow=False,
        font=dict(size=16, color=font_color, family=font_family),
        align="center"
    )

    fig.update_layout(
            xaxis=dict(
                tickfont=dict(size=14, color= "white", family=font_family)  # Change "red" to any color you like
            ),
            yaxis=dict(
                tickfont=dict(color="white")
            )

        )

    # Update layout with increased height, font size, and grid lines
    fig.update_layout(
        title="Cost of Selected Methods",
        xaxis={'title': 'Category'},
        yaxis={
            'title': 'Cost',
            'range': [0, 15],  # Adjust y-axis range for smaller prices
            'gridcolor': 'darkgray'  # Grid line color
        },
        barmode='group',  # Group bars side by side
        height=600,  # Make the graph taller
        width=800,
        margin=dict(t=80, b=40, l=40, r=40),  # Adjust margins
        title_font=dict(size=24, color=font_color, family=font_family),  # Larger title font size
        xaxis_title_font=dict(size=18, color=font_color, family=font_family),  # X-axis title font size
        yaxis_title_font=dict(size=18, color=font_color, family=font_family),  # Y-axis title font size
        legend=dict(font=dict(size=14, color=font_color, family=font_family)),  # Legend font size
        paper_bgcolor= bg_color,  # Background color of the entire figure
        shapes=[{
        'type': 'rect',
        'x0': 0, 'y0': 0,
        'x1': 1, 'y1': 1,
        'xref': 'paper', 'yref': 'paper',
        'line': {
            'color': 'black',
            'width': 2,
        }
    }]
    )
    
    return fig

=======
displayCostGraph(app, costData)

update_cost_graph(app)
update_revenue_graph(app)
>>>>>>> 1b3524d1d217fbb31407e1f314c6ddbbeffefd3c

# Run the app
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) #use for render hosting
    app.run_server(debug=True) #use for local development
