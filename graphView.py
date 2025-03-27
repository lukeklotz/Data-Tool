from costData import *

def displayCostGraph(app, costData, revData):

    # group cost data
    backContactCost = costData.getBackContact() 
    absorberCost    = costData.getAbsorber() 
    glassCost       = costData.getGlass()       
    HTLayerCost     = costData.getHTLayer()

    # group revenue data
    '''
    backContactRev = revData.getBackContact()
    absorberRev    = revData.getAbsorber()
    glassRev       = revData.getGlass()
    '''
    #drop down and background styles
    width            = '90%'
    #dd_color         = '#353431'
    #bg_color         = '#23221B'
    #background_color = '#8E9FA3'

    #bar graph styles
    #font_color  = "#afa732"
    #font_family = "Courier New"


    # -  step 1 methods - #
    backContactHtml = ["Aluminum", "Gold", "Silver", "Copper", "Carbon"]
    htlHTML         = ["Free", "Spiro-OmETAD", "CuSCN", "NiO"]
    absorberHTML    = ["MAPbI₃"]
    etlHTML         = ["TiO₂", "SnO₂"]
    coatedGlassHTML         = ["Coated Glass"]


    # - step 2 methods - #

    step2BackContactHTML = ["Chemical", "Physical", "Physical", "Chemical", "Physical / Chemical", "Physical / Chemical"]
    step2AbsorberHTML    = ["Hydrogen Iodide",
                            "DMF",
                            "Ion Exchange",
                            "Potassium Iodide",
                            "DMF",
                            "Aqueous dissolution",
                            "Chlorobenzene"]
    step2CoatedGlass    = ["Butylamine",
                           "DMF",
                           "Ethyl Acetate",
                           "Potassium Iodide",
                           "DMF",
                           "Chlorobenzene",
                           "NaOAc, Nal, H₃PO₂ in water",
                           "Chlorobenzene"]

    backContactLit  = ["Feng et al. 2021",
                       "Ren et al. 2021",
                       "Kim et al. 2023",
                       "O Hara et al. 2023",
                       "Xiao et al. 2025",
                       "Wu et al. 2024"]
    absorberLit     = ["Feng et al. 2021",
                       "Deng et al. 2022",
                       "Ren et al. 2021",
                       "O'Hara et al. 2023",
                       "Bo Chen et al. 2021",
                       "Xiao et al. 2025",
                       "Wu et al. 2024"]
    CoatedGlassLit  = ["Feng et al. 2021",
                       "Deng et al. 2022",
                       "Ren et al. 2021",
                       "O'hara et al. 2023",
                       "Kim et al. 2023",
                       "Bo Chen et al. 2022",
                       "Xiao et al. 2025",
                       "Wu et al. 2024"]

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
                
                html.Section([
                    html.Div([
                        html.Div("Layer"), 
                        html.Div("Alternative Materials")
                    ], className="layer-info-row"),

                    html.Div([
                        html.Div("Back Contact Layer"),
                            html.Div([html.Div(material, className="layer-info-item") for material in backContactHtml], className="layer-info-col"),
                    ], className="layer-info-row"),
                     
                    html.Div([
                        html.Div("Hole Transport Layer"),
                            html.Div([html.Div(material) for material in htlHTML], className="layer-info-col"),

                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("Absorber"),
                            html.Div([html.Div(material) for material in absorberHTML], className="layer-info-col"),
                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("ETL"),
                            html.Div([html.Div(material) for material in etlHTML], className="layer-info-col"),
                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("FTO Coated Glass"),
                            html.Div([html.Div(material) for material in coatedGlassHTML], className="layer-info-col"),
                    ], className="layer-info-row"),

                ], className="layer-info-box-1")
            ], className="box-common box-mid"),


            html.Div([
                html.H3("Step 2: Selection of Extraction Method", className="materials-title"),
                #html.Img(src="/assets/text.png", alt="img_2", className="box-image")
                html.Section([
                    html.Div([
                        html.Div("Layer"), 
                        html.Div("Method"),
                        html.Div("Literature")
                    ], className="layer-info-row"), 
                     
                    html.Div([
                        html.Div("Back Contact"),
                            html.Div([html.Div(material) for material in step2BackContactHTML], className="layer-info-col"),
                            html.Div([html.Div(literature) for literature in backContactLit], className="layer-info-col"),

                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("Absorber"),
                            html.Div([html.Div(material) for material in step2AbsorberHTML], className="layer-info-col"),
                            html.Div([html.Div(literature) for literature in absorberLit], className="layer-info-col")
                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("ETL / Coated Glass"),
                            html.Div([html.Div(material) for material in step2CoatedGlass], className="layer-info-col"),
                            html.Div([html.Div(literature) for literature in CoatedGlassLit], className="layer-info-col")
                    ], className="layer-info-row"),

                ], className="layer-info-box-1")
            ], className="box-common box-mid"),
            ], className="materials-container"),
        ], className="top-row-container"),

    #graph styling
    html.Section([

    #cost Graph
    html.Div([
        # Column 1: Dropdowns and titles
        html.Div([

            html.H4("HTL", className='dropdown'),
            dcc.Dropdown(
                id='HTL-dropdown',
                options=[{'label': k, 'value': k} for k in HTLayerCost.keys()],
                value=list(HTLayerCost.keys())[0],   # gets first value (default)
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

    ], className="graph-and-dropdown-container bar-graph"),

    # Revenue Graph
    html.Div([
        
        html.Div([

            
        ], className="dd-width-padding revenue"), 
       
       html.Div([
            dcc.Graph(
                id='cost-revenue-chart')
        ], className="drop-down-menu-"),

    ], className="graph-and-dropdown-container bar-graph revenue"),


    ], className="graph-and-dropdown-container")
    

], className="background")





