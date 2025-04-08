from costData import *

def displayCostGraph(app, costData, revData):

    # group cost data
    backContactCost = costData.getBackContact() 
    absorberCost    = costData.getAbsorber() 
    glassCost       = costData.getGlass()       
    HTLayerCost     = costData.getHTLayer()

    # width of dropdown menus
    width            = '90%'

    # -  step 1 methods - #
    backContactHtml = ["Aluminum", "Gold", "Silver", "Copper", "Carbon"]
    htlHTML         = ["Free", "Spiro-OmETAD", "CuSCN", "NiO"]
    absorberHTML    = ["MAPbI₃"]
    etlHTML         = ["TiO₂", "SnO₂"]
    coatedGlassHTML = ["Coated Glass"]


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
                       "O'Hara et al. 2023",
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
                       "O'Hara et al. 2023",
                       "Kim et al. 2023",
                       "Bo Chen et al. 2021",
                       "Xiao et al. 2025",
                       "Wu et al. 2024"]
    
    lit_urls = {
        "Feng et al. 2021": "https://www.sciencedirect.com/science/article/pii/S2666386421000266?via%3Dihub",
        "Deng et al. 2022": "https://pubs.acs.org/doi/10.1021/acsami.2c14638?ref=pdf",
        "Bo Chen et al. 2021": "https://www.nature.com/articles/s41467-021-26121-1",
        "Ren et al. 2021": "https://pubs.acs.org/doi/10.1021/acssuschemeng.1c07083?ref=pdf",
        "Kim et al. 2023": "https://pubs.acs.org/doi/10.1021/acsenergylett.3c01542?ref=pdf",
        "O'Hara et al. 2023": "https://link.springer.com/article/10.1557/s43580-023-00559-5",
        "Xiao et al. 2025": "https://example.com/xiao2025",
        "Wu et al. 2024": "https://pubs.rsc.org/en/content/articlelanding/2024/ee/d4ee01071j",
    }

    app.layout = html.Div([
        
        html.Div([
            html.Div([
                html.H1("Assumptions for Tool", className="big-font"),
                html.P("1. The volume of chemicals applied was determined by completely submerging the 1m2 module plus 10% volume on the surface area, totaling 3.9L.", className="top"),
                html.P("2. The methods were modeled following literature and applying large scale applications. ", className="top"),
                html.P("3. The prices of chemicals were obtained from commercial suppliers (Sigma Aldrich, Alibaba, and ChemAnaylst) to reflect bulk chemical prices for large scale recycling. ", className="top"),
                html.P("4. The price of 1 kWh of energy was taken from the most up-to-date cost of industrial electricity at $0.073/kWh  ", className="top"),
                html.P("5. The model build does not include frame, cables, and junctions. ", className="top"),
                html.A("(This project was funded by the NSF grant #2403520)", href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2403520&HistoricalAwards=false", className="top nsf"),
                
            ], className="box-common box-top"),

        html.Div([
            html.Div([
                html.H3("Input: Selection of Extraction Method", className="materials-title"),
                html.Section([
                    html.Div([
                        html.Div("Layer"), 
                        html.Div("Method"),
                        html.Div("Literature")
                    ], className="layer-info-row"), 
                     
                    html.Div([
                        html.Div("Back Contact"),
                            html.Div([html.Div(material) for material in step2BackContactHTML], className="layer-info-col"),
                            html.Div([html.A(literature, href=lit_urls[literature], target="_blank") for literature in backContactLit], className="layer-info-col"),

                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("Absorber"),
                            html.Div([html.Div(material) for material in step2AbsorberHTML], className="layer-info-col"),
                            html.Div([html.A(literature, href=lit_urls[literature], target="_blank") for literature in absorberLit], className="layer-info-col")
                    ], className="layer-info-row"),
                    html.Div([
                        html.Div("ETL / Coated Glass"),
                            html.Div([html.Div(material) for material in step2CoatedGlass], className="layer-info-col"),
                            html.Div([html.A(literature, href=lit_urls[literature], target="_blank") for literature in CoatedGlassLit], className="layer-info-col")
                    ], className="layer-info-row"),

                ], className="layer-info-box-1")
            ], className="box-common box-mid input"),

            html.Div([
                html.H3("Output: Total Revenue of Selected Methods", className="materials-title"),
                
                html.Section([
                    html.Div([
                        html.Div("Layer"), 
                        html.Div("Alternative Materials")
                    ], className="layer-info-row"),

                    html.Div([
                        html.Div("Hole Transport Layer (HTL)"),
                            html.Div([html.Div(material) for material in htlHTML], className="layer-info-col"),

                    ], className="layer-info-row"),

                    html.Div([
                        html.Div("Back Contact Layer"),
                            html.Div([html.Div(material, className="layer-info-item") for material in backContactHtml], className="layer-info-col"),
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
        ], className="drop-down-menu revenue"),

    ], className="graph-and-dropdown-container bar-graph revenue"),

    ], className="graph-and-dropdown-container")
    
], className="background")





