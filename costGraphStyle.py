from costData import *

def displayCostGraph(app, coverGlass, backContact, absorber, etl, width, dd_color, font_color, bg_color):

    print(f"coverGlass: {coverGlass["Cost"].values}")
    app.layout = html.Div([
        
        html.Div([
            html.Div([
                html.H1("Assumptions for Tool", className="big-font"),
                html.P("1. The volume of chemicals applied was determined by completely submerging the 1m2 module plus 10% volume on the surface area, totaling 3.9L.", className="top"),
                html.P("2. The methods were modeled following literature and applying large scale applications. ", className="top"),
                html.P("3. The price of chemicals was taken from commercial suppliers (Sigma Aldrich, Alibaba, and ChemAnaylst) to utilize bulk chemicals prices for large scale recycling. ", className="top"),
                html.P("4. The price of 1 kWh of energy was taken from the most up-to-date cost of industrial electricity at $0.073/kWh  ", className="top"),
                html.P("5. The model build does not include frame, cables, and junctions. ", className="top"),
            ], className="box-common box-top"),
        ], className="materials-container"),

        html.Div([
            html.Div([
                html.H3("Step 1: Selection of Materials", className="dropdown"),
                html.Img(src="/assets/graphic.png", alt="img_1", className="box-image")
            ], className="box-common box-mid"),
            html.Div([
                html.H3("Step 2: Selection of Extraction Method", className="dropdown"),
                html.Img(src="/assets/text.png", alt="img_2", className="box-image")
            ], className="box-common box-mid"),
        ], className="materials-container"),

    html.Div([
        # Column 1: Dropdowns and titles
        html.Div([
            html.H4("Cover Glass", className='dropdown'),
            dcc.Dropdown(
                id='coverGlass-dropdown',
                options=[{'label': method, 'value': method} for method in coverGlass["Method"].values],
                value=coverGlass["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("Back Contact", className='dropdown'),
            dcc.Dropdown(
                id='backContact-dropdown',
                options=[{'label': method, 'value': method} for method in backContact["Method"].values],
                value=backContact["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("Absorber", className='dropdown'),
            dcc.Dropdown(
                id='Absorber-dropdown',
                options=[{'label': method, 'value': method} for method in absorber["Method"].values],
                value=absorber["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("ETL/Coated Glass", className='dropdown'),
            dcc.Dropdown(
                id='etl-dropdown',
                options=[{'label': method, 'value': method} for method in etl["Method"].values],
                value=etl["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
        ], style={'width': '30%', 'padding': '20px'}),  # 30% width for dropdowns and titles
        

        html.Div([
            dcc.Graph(id='cost-bar-chart')
        ], style={'width': '50%', 'padding-left': '30px',         #dropdown menu
                  'display': 'flex', 'justify-content': 'center', 
                  'align-items': 'center',
                  'background': dd_color,
                  'color': font_color}), 

    ], style={'background': dd_color, 'display': 'flex',          #graph and dropdown container
              'align-items': 'flex-start', 
              'justify-content': 'center', 
              'width': '90%',
              'border-radius': '15px',
              'border': 'solid black 2px',
              'padding': '25px',
              'margin-bottom': '50px'}), 

], style={'display': 'flex', 'flex-direction': 'column',          #background
          'align-items': 'center', 'justify-content': 'center', 
          'height': '100%',
          'background': bg_color,
          'padding': '0',
          'margin': '0',
          })  