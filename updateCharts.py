import plotly.graph_objects as go
from graphView import * 
from revenueData import *
from utils import *


#drop down and background styles
width            = '70%'
dd_color         = '#353431'
bg_color         = '#17171a'
background_color = '#8E9FA3'
accent_color     = '#3d3c36'

color_white      = '#ffffff'

barColor1 = '#82A66F'
barColor2 = '#6F8EA6'
barColor3 = '#BBB775'
barColor4 = '#A66F6F'
barColor5 = '#6FA697' 

#bar graph styles
#font_color  = "#afa732"   # mustard-yellow
font_color   = "#ffffff" # white
font_family = "Courier New"

def update_cost_graph(app):
    cost = costData()    #extract data from costData class

    @app.callback(
        Output('cost-bar-chart', 'figure'),
        [
            Input('coverGlass-dropdown', 'value'),
            Input('backContact-dropdown', 'value'),
            Input('Absorber-dropdown', 'value'),
            Input('etl-dropdown', 'value')
        ]
    )

    def update_graph(coverGlass_method, backContact_method, absorber_method, glass_method):

        coverGlassCost = cost.getCoverGlassCost(coverGlass_method)
        backContactCost = cost.getBackContactCost(backContact_method)
        absorberCost = cost.getAbsorberCost(absorber_method)
        glassCost = cost.getGlassCost(glass_method)

        formatted_total_cost = formatTotalCost(coverGlassCost, backContactCost, absorberCost, glassCost)
        
        # Create the bar chart
        fig = go.Figure()

        bar_title_font_style = dict(size=12, color=font_color, family=font_family)

        fig.add_trace(go.Bar(
            x=["Cover Glass"],
            y=[coverGlassCost],
            name="Cover Glass",
            marker=dict(color=barColor1, line=dict(width=2, color="black")),
            text=[f"${coverGlassCost}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Back Contact"],
            y=[backContactCost],
            name="Back Contact",
            marker=dict(color=barColor2, line=dict(width=2, color="black")),
            text=[f"${backContactCost}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Absorber"],
            y=[absorberCost],
            name="Absorber",
            marker=dict(color=barColor3, line=dict(width=2, color="black")),
            text=[f"${absorberCost}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["ETL"],
            y=[glassCost],
            name="ETL",
            marker=dict(color=barColor4, line=dict(width=2, color="black")),
            text=[f"${glassCost}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Total"],
            y=[formatted_total_cost],
            name="Total Cost",
            marker=dict(color=barColor5, line=dict(width=2, color="black")),
            text=[f"${formatted_total_cost}"],
            textposition="outside",
            textfont=bar_title_font_style
        ))

        # Update layout for the total
        fig.add_annotation(
            text=f"Total: ${formatted_total_cost}",
            xref="paper", yref="paper",
            x=1.29, y=0.0,
            showarrow=False,
            font=dict(size=16, color=font_color, family=font_family),
            align="center"
        )

        fig.update_layout(
            title=dict(
                text="Cost of Selected Methods",
                x=0.5,
                xanchor='center',
            ),
            xaxis={
                #'title': 'Method',
                'tickfont': dict(color=font_color, family=font_family),
                'showgrid': False,  # Remove vertical grid lines for cleaner look
                'linecolor': font_color,  # Match axis line to text color
                'tickangle': 0,  # Angle labels for better readability if you have long method names
                'ticks': 'outside',  # Place ticks outside
                'tickwidth': 2,  # Make ticks more visible
                'tickcolor': font_color  # Match tick color to text
            },
            yaxis={
                'title': 'Cost $/m²', 
                'range': [0, 16], 
                'gridcolor': accent_color,
                'tickfont': dict(color=font_color, family=font_family),
                'tickprefix': '$',  # Add dollar sign for cost values
                'tickmode': 'linear',
                'dtick': 2,  # Tick every $2 for cleaner appearance
                'linecolor': font_color,  # Match axis line to text color
                'ticks': 'outside',
                'tickwidth': 2,
                'tickcolor': font_color
            },
            barmode='group',
            bargap=0.15,  # Adjust spacing between bar groups
            bargroupgap=0.05,  # Adjust spacing between bars within groups
            margin=dict(t=120, b=40, l=60, r=40),  # Slightly larger bottom and left margins
            autosize=True,
            title_font=dict(size=24, color=font_color, family=font_family),
            xaxis_title_font=dict(size=18, color=font_color, family=font_family),
            yaxis_title_font=dict(size=18, color=font_color, family=font_family),
            legend=dict(
                font=dict(size=14, color=font_color, family=font_family),
                bgcolor='rgba(0,0,0,0.1)',  # Semi-transparent background
                bordercolor=font_color,
                borderwidth=1,
                orientation='h',  # Horizontal legend
                yanchor='top',
                y=1.15,  # Position above the chart
                xanchor='center',
                x=0.5
            ),
            paper_bgcolor=bg_color,
            plot_bgcolor=bg_color,  # Match plot background to paper background
            height=500,
            uniformtext=dict(mode='hide', minsize=10),  # Ensures uniform text size
        )

        return fig
    
def update_revenue_graph(app):
    revData = revenueData()  
    cost = costData()

    @app.callback(
        Output('cost-revenue-chart', 'figure'),
        [
            Input('cg-revenue-dropdown', 'value'),

            Input('backContact-dropdown', 'value'),  #input is from cost graph
            Input('Absorber-dropdown', 'value'),
            
            Input('etl-revenue-dropdown', 'value')  
        ]
    )
    def update_graph(coverGlass_method, backContact_method, absorber_method, glass_method):

        
        coverGlassCost = revData.getCoverGlassRev(coverGlass_method)

        backContactCost = revData.getBackContactRev(backContact_method)
        absorberCost = revData.getAbsorberRev(absorber_method)

        glassCost = revData.getGlassRev(glass_method)

        # Calculate total cost
        formatted_total_cost = coverGlassCost + backContactCost + absorberCost + glassCost

        # Create the bar chart
        fig = go.Figure()

        bar_title_font_style = dict(size=12, color=font_color, family=font_family)

        fig.add_trace(go.Bar(
            x=["Cover Glass"],
            y=[coverGlassCost],
            name="Cover Glass",
            marker=dict(color=barColor1, line=dict(width=2, color="black")),
            text=[f"${coverGlassCost:.2f}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Back Contact"],
            y=[backContactCost],
            name="Back Contact",
            marker=dict(color=barColor2, line=dict(width=2, color="black")),
            text=[f"${backContactCost:.2f}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Absorber"],
            y=[absorberCost],
            name="Absorber",
            marker=dict(color=barColor3, line=dict(width=2, color="black")),
            text=[f"${absorberCost:.2f}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Glass"],
            y=[glassCost],
            name="Glass",
            marker=dict(color=barColor4, line=dict(width=2, color="black")),
            text=[f"${glassCost:.2f}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Total"],
            y=[formatted_total_cost],
            name="Total Cost",
            marker=dict(color=barColor5, line=dict(width=2, color="black")),
            text=[f"${formatted_total_cost:.2f}"],
            textposition="outside",
            textfont=bar_title_font_style
        ))

        # Update layout for the graph
        fig.add_annotation(
            text=f"Total: ${formatted_total_cost:.2f}",
            xref="paper", yref="paper",
            x=1.29, y=0.0,
            showarrow=False,
            font=dict(size=16, color=font_color, family=font_family),
            align="center"
        )

        fig.update_layout(
            title=dict(
                text="Revenue of Selected Methods",
                x=0.5,
                xanchor='center',
            ),
            xaxis={
                'tickfont': dict(color=font_color, family=font_family),
                'showgrid': False,  # Remove vertical grid lines for cleaner look
                'linecolor': font_color,  # Match axis line to text color
                'tickangle': 0,  # Angle labels for better readability if you have long method names
                'ticks': 'outside',  # Place ticks outside
                'tickwidth': 2,  # Make ticks more visible
                'tickcolor': font_color  # Match tick color to text
            },
            yaxis={
                'title': 'Revenue $/m²', 
                'range': [0, 20], 
                'gridcolor': accent_color,
                'tickfont': dict(color=font_color, family=font_family),
                'tickprefix': '$',  # Add dollar sign for cost values
                'tickmode': 'linear',
                'dtick': 2,  # Tick every $2 for cleaner appearance
                'linecolor': font_color,  # Match axis line to text color
                'ticks': 'outside',
                'tickwidth': 2,
                'tickcolor': font_color,
            },
            barmode='group',
            bargap=0.15,  # Adjust spacing between bar groups
            bargroupgap=0.05,  # Adjust spacing between bars within groups
            margin=dict(t=120, b=40, l=60, r=40),  # Slightly larger bottom and left margins
            autosize=True,
            title_font=dict(size=24, color=font_color, family=font_family),
            xaxis_title_font=dict(size=18, color=font_color, family=font_family),
            yaxis_title_font=dict(size=18, color=font_color, family=font_family),
            legend=dict(
                font=dict(size=14, color=font_color, family=font_family),
                bgcolor='rgba(0,0,0,0.1)',  # Semi-transparent background
                bordercolor=font_color,
                borderwidth=1,
                orientation='h',  # Horizontal legend
                yanchor='top',
                y=1.15,  # Position above the chart
                xanchor='center',
                x=0.5
            ),
            paper_bgcolor=bg_color,
            plot_bgcolor=bg_color,  # Match plot background to paper background
            height=500, 
            uniformtext=dict(mode='hide', minsize=10),  # Ensures uniform text size
        )

        return fig