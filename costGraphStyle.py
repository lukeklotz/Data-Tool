from costDataJuan import *

def displayCostGraph(app, costData, revData):

    # group cost data
    coverGlassCost  = costData.getCoverGlass()
    backContactCost = costData.getBackContact() 
    absorberCost    = costData.getAbsorber() 
    glassCost       = costData.getGlass()       

    # group revenue data

    coverGlassRev  = revData.getCoverGlass()
    backContactRev = revData.getBackContact()
    absorberRev    = revData.getAbsorber()
    glassRev       = revData.getGlass()

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

        html.Div([
            html.Div([
                html.H3("Step 1: Selection of Materials", className="materials-title"),
                html.Img(src="/assets/graphic.png", alt="img_1", className="box-image")
            ], className="box-common box-mid"),
            html.Div([
                html.H3("Step 2: Selection of Extraction Method", className="materials-title"),
                html.Img(src="/assets/text.png", alt="img_2", className="box-image")
            ], className="box-common box-mid"),
            ], className="materials-container"),
        ], className="top-row-container"),

    #cost graph styling
    html.Div([
        # Column 1: Dropdowns and titles
        html.Div([
            html.H4("Cover Glass", className='dropdown'),
            dcc.Dropdown(
                id='coverGlass-dropdown',
                options=[{'label': k, 'value': k} for k in coverGlassCost.keys()],
                value=list(coverGlassCost.keys())[0],  # gets first value (default)
                style={'width': width}
            ),
            
            html.H4("Back Contact", className='dropdown'),
            dcc.Dropdown(
                id='backContact-dropdown',
                options=[{'label': k, 'value': k} for k in backContactCost.keys()],
                value=list(backContactCost.keys())[0],   # gets first value (default)
                style={'width': width}
            ),
            
            html.H4("Absorber", className='dropdown'),
            dcc.Dropdown(
                id='Absorber-dropdown',
                options=[{'label': k, 'value': k} for k in absorberCost.keys()],
                value=list(absorberCost.keys())[0],   # gets first value (default)
                style={'width': width}
            ),
            
            html.H4("ETL/Coated Glass", className='dropdown'),
            dcc.Dropdown(
                id='etl-dropdown',
                options=[{'label': k, 'value': k} for k in glassCost.keys()],
                value=list(glassCost.keys())[0],   # gets first value (default)
                style={'width': width}
            ),
            
        ], className="dd-width-padding"), 

        html.Div([
            dcc.Graph(id='cost-bar-chart'),
        ], className="drop-down-menu"),

    ], className="graph-and-dropdown-container"),

    # Initialize app layout
    html.Div([
        html.Div([
            html.H4("Cover Glass", className='dropdown'),
            dcc.Dropdown(
                id='c-dropdown',
                options=[{'label': k, 'value': k} for k in coverGlassRev.keys()],
                value=list(coverGlassRev.keys())[0],  # Default value
                style={'width': width}
            ),

            html.H4("Back Contact", className='dropdown'),
            dcc.Dropdown(
                id='b-dropdown',
                options=[{'label': k, 'value': k} for k in backContactRev.keys()],
                value=list(backContactRev.keys())[0],
                style={'width': width}
            ),

            html.H4("Absorber", className='dropdown'),
            dcc.Dropdown(
                id='A-dropdown',
                options=[{'label': k, 'value': k} for k in absorberRev.keys()],
                value=list(absorberRev.keys())[0],
                style={'width': width}
            ),

            html.H4("Glass", className='dropdown'),
            dcc.Dropdown(
                id='e-dropdown',
                options=[{'label': k, 'value': k} for k in glassRev.keys()],
                value=list(glassRev.keys())[0],
                style={'width': width}
            ),
        ], className="dd-width-padding"), 

        html.Div([
            dcc.Graph(
                id='cost-revenue-chart',)
        ], className="drop-down-menu"),
    ], className="graph-and-dropdown-container")


], className="background")





