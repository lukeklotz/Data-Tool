from costData import *

def displayCostGraph(app, costData, revData):

    # group cost data
    coverGlass  = costData.getCoverGlass()
    backContact = costData.getBackContact() 
    absorber    = costData.getAbsorber() 
    etl         = costData.getEtl() 

    # group revenue data

    coverGlassRev = revData.getCoverGlassRev()
    backContectRev = revData.getBackContactRev()
    absorberRev = revData.getAbsorberRev()
    glassRev = revData.getGlassRev()

    #drop down and background styles
    width            = '70%'
    dd_color         = '#353431'
    bg_color         = '#23221B'
    background_color = '#8E9FA3'

    #bar graph styles
    font_color  = "#afa732"
    font_family = "Courier New"

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

    #cost graph styling
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
            
        ], className="dd-width-padding"), 

        html.Div([
            dcc.Graph(id='cost-bar-chart')
        ], className="drop-down-menu"),

    ], className="graph-and-dropdown-container"),

    #revenue graph styling
    html.Div([
        # Column 1: Dropdowns and titles
        html.Div([
            html.H4("Cover Glass", className='dropdown'),
            dcc.Dropdown(
                id='c-dropdown',
                options=[{'label': method, 'value': method} for method in coverGlass["Method"].values],
                value=coverGlass["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("Back Contact", className='dropdown'),
            dcc.Dropdown(
                id='b-dropdown',
                options=[{'label': method, 'value': method} for method in backContact["Method"].values],
                value=backContact["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("Absorber", className='dropdown'),
            dcc.Dropdown(
                id='A-dropdown',
                options=[{'label': method, 'value': method} for method in absorber["Method"].values],
                value=absorber["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
            html.H4("ETL/Coated Glass", className='dropdown'),
            dcc.Dropdown(
                id='e-dropdown',
                options=[{'label': method, 'value': method} for method in etl["Method"].values],
                value=etl["Method"].values[0],  # Default value
                style={'width': width}
            ),
            
        ], className="dd-width-padding"), 

        html.Div([
            dcc.Graph(id='cost-revenue-chart')
        ], className="drop-down-menu"),

    ], className="graph-and-dropdown-container"),


], className="background")





