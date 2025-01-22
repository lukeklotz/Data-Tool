import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback


def displayBarGraph(app, coverGlass_methods, backContact_methods, Absorber_methods, etl_methods, width, dd_color, font_color, bg_color):

    app.layout = html.Div([

        html.Div([
            html.Div(className="box"),
            html.Div(className="box"),
        ], className="materials-container"), 

    html.Div([
        # Column 1: Dropdowns and titles
        html.Div([
            html.H4("Cover Glass", className='dropdown'),
            dcc.Dropdown(
                id='coverGlass-dropdown',
                options=[{'label': method, 'value': method} for method in coverGlass_methods],
                value=coverGlass_methods[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("Back Contact", className='dropdown'),
            dcc.Dropdown(
                id='backContact-dropdown',
                options=[{'label': method, 'value': method} for method in backContact_methods],
                value=backContact_methods[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("Absorber", className='dropdown'),
            dcc.Dropdown(
                id='Absorber-dropdown',
                options=[{'label': method, 'value': method} for method in Absorber_methods],
                value=Absorber_methods[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("ETL/Coated Glass", className='dropdown'),
            dcc.Dropdown(
                id='etl-dropdown',
                options=[{'label': method, 'value': method} for method in etl_methods],
                value=etl_methods[0],  # Default value
                style={'width': width}
            ),
            
        ], style={'width': '30%', 'padding': '20px'}),  # 30% width for dropdowns and titles
        
        # Column 2: The Graph
        html.Div([
            dcc.Graph(id='cost-bar-chart')
        ], style={'width': '50%', 'padding-left': '30px', #dropdown menu
                  'display': 'flex', 'justify-content': 'center', 
                  'align-items': 'center',
                  'background': dd_color,
                  'color': font_color}),  # Flexbox to center the graph
    ], style={'background': dd_color, 'display': 'flex', #graph and dropdown container
              'align-items': 'flex-start', 
              'justify-content': 'center', 
              'width': '90%',
              'border-radius': '15px',
              'border': 'solid black 2px',
              'padding': '25px'}),  # Flexbox layout to align side by side and center horizontally


], style={'display': 'flex', 'flex-direction': 'column', #background
          'align-items': 'center', 'justify-content': 'center', 
          'height': '100vh',
          'background': bg_color,
          'padding': '0',
          'margin': '0',
          })  # Outer Div to center everything on the page