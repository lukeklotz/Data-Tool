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
font_color   = "#ffffff" # white
font_family = "Courier New"

def update_cost_graph(app):
    cost = costData()    #extract data from costData class

    @app.callback(
        Output('cost-bar-chart', 'figure'),
        [
            Input('HTL-dropdown', 'value'),
            Input('backContact-dropdown', 'value'),
            Input('Absorber-dropdown', 'value'),
            Input('etl-dropdown', 'value'),
        ]
    )

    def update_graph(htl_method, backContact_method, absorber_method, glass_method):

        backContactCost = cost.getBackContactCost(backContact_method)
        absorberCost    = cost.getAbsorberCost(absorber_method)
        glassCost       = cost.getGlassCost(glass_method)
        htlCost         = cost.getHTLayerCost(htl_method)

        formatted_total_cost = formatTotalCost(htlCost, backContactCost, absorberCost, glassCost)
        
        # Create the bar chart
        fig = go.Figure()


        #dynamically update range bounds based on formatted_total_cost
        range_bounds = [0, 16]

        if formatted_total_cost > 16:
            range_bounds = [0, 20]
        else:
            range_bounds = [0, 16]

        bar_title_font_style = dict(size=12, color=font_color, family=font_family)
 
        fig.add_trace(go.Bar(
            x=["HTL"],
            y=[htlCost],
            name="HTL",
            marker=dict(color=barColor1, line=dict(width=2, color="black")),
            text=[f"${htlCost}"],
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
                'title': 'Method',
                'tickfont': dict(color=font_color, family=font_family),
                'showgrid': False,  
                'linecolor': font_color,  
                'tickangle': 0,  
                'ticks': 'outside',  
                'tickwidth': 2,  
                'tickcolor': font_color  
            },
            yaxis={
                'title': 'Cost $/m²', 
                'range': range_bounds, 
                'gridcolor': accent_color,
                'tickfont': dict(color=font_color, family=font_family),
                'tickprefix': '$',  
                'tickmode': 'linear',
                'dtick': 2,  
                'linecolor': font_color,  
                'ticks': 'outside',
                'tickwidth': 2,
                'tickcolor': font_color
            },
            barmode='group',
            bargap=0.15,  
            bargroupgap=0.05,  
            margin=dict(t=120, b=40, l=60, r=40),  
            autosize=True,
            title_font=dict(size=24, color=font_color, family=font_family),
            xaxis_title_font=dict(size=18, color=font_color, family=font_family),
            yaxis_title_font=dict(size=18, color=font_color, family=font_family),
            legend=dict(
                font=dict(size=14, color=font_color, family=font_family),
                bgcolor='rgba(0,0,0,0.1)',  
                bordercolor=font_color,
                borderwidth=1,
                orientation='h',  
                yanchor='top',
                y=1.15,  
                xanchor='center',
                x=0.5
            ),
            paper_bgcolor=bg_color,
            plot_bgcolor=bg_color,  
            height=500,
            uniformtext=dict(mode='hide', minsize=10),  
        )

        return fig
    
def update_revenue_graph(app):
    revData = revenueData()  

    @app.callback(
        Output('cost-revenue-chart', 'figure'),
        [   Input('HTL-dropdown', 'value'),
            Input('backContact-dropdown', 'value'),  #input is from cost graph
            Input('Absorber-dropdown', 'value'),
            Input('etl-dropdown', 'value')  
        ]
    )
    def update_graph(htl_method, backContact_method, absorber_method, glass_method):

        
        htlRev          = revData.getHTLayerRev(htl_method)
        backContactCost = revData.getBackContactRev(backContact_method)
        absorberCost    = revData.getAbsorberRev(absorber_method)
        glassCost       = revData.getGlassRev(glass_method)

        # Calculate total cost
        formatted_total_cost = htlRev + backContactCost + absorberCost + glassCost


        #update range and tick dynamically based on formatted_total_cost
        range_bounds = [0, 20]
        tick_range = 2

        if formatted_total_cost > 40:
            range_bounds = [0, 120]
            tick_range = 10
        else:
            range_bounds = [0, 20]
            tick_range = 2

        # Create the bar chart
        fig = go.Figure()

        bar_title_font_style = dict(size=12, color=font_color, family=font_family)

        fig.add_trace(go.Bar(
            x=[revData.getHTLayerType(htl_method)],
            y=[htlRev],
            name="HTL",
            marker=dict(color=barColor1, line=dict(width=2, color="black")),
            text=[f"${htlRev:.2f}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))


        fig.add_trace(go.Bar(
            x=[revData.getBackContactType(backContact_method)],
            y=[backContactCost],
            name="Back Contact",
            marker=dict(color=barColor2, line=dict(width=2, color="black")),
            text=[f"${backContactCost:.2f}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=[revData.getAbsorberType(absorber_method)],
            y=[absorberCost],
            name="Absorber",
            marker=dict(color=barColor3, line=dict(width=2, color="black")),
            text=[f"${absorberCost:.2f}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=[revData.getGlassType(glass_method)],
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
                'showgrid': False,  
                'linecolor': font_color,  
                'tickangle': 0,  
                'ticks': 'outside',  
                'tickwidth': 2,  
                'tickcolor': font_color  
            },
            yaxis={
                'title': 'Revenue $/m²', 
                'range': range_bounds, 
                'gridcolor': accent_color,
                'tickfont': dict(color=font_color, family=font_family),
                'tickprefix': '$',  
                'tickmode': 'linear',
                'dtick': tick_range,  
                'linecolor': font_color,  
                'ticks': 'outside',
                'tickwidth': 2,
                'tickcolor': font_color,
            },
            barmode='group',
            bargap=0.15,  
            bargroupgap=0.05,  
            margin=dict(t=120, b=40, l=60, r=40),  
            autosize=True,
            title_font=dict(size=24, color=font_color, family=font_family),
            xaxis_title_font=dict(size=18, color=font_color, family=font_family),
            yaxis_title_font=dict(size=18, color=font_color, family=font_family),
            legend=dict(
                font=dict(size=14, color=font_color, family=font_family),
                bgcolor='rgba(0,0,0,0.1)',  
                bordercolor=font_color,
                borderwidth=1,
                orientation='h',  
                yanchor='top',
                y=1.15,  
                xanchor='center',
                x=0.5
            ),
            paper_bgcolor=bg_color,
            plot_bgcolor=bg_color,  
            height=500, 
            uniformtext=dict(mode='hide', minsize=10),  
        )

        return fig