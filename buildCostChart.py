from utils import *
import plotly.graph_objects as go


#drop down and background styles
width            = '70%'
dd_color         = '#353431'
bg_color         = '#23221B'
background_color = '#8E9FA3'

#bar graph styles
font_color  = "#afa732"
font_family = "Courier New"

def update_cost_graph(app):

    @app.callback(
        Output('cost-bar-chart', 'figure'),
        [
            Input('coverGlass-dropdown', 'value'),
            Input('backContact-dropdown', 'value'),
            Input('Absorber-dropdown', 'value'),
            Input('etl-dropdown', 'value')
        ]
    )

    def update_graph(coverGlass_method, backContact_method, absorber_method, etl_method):

        coverGlassCost = getCoverGlassCost(coverGlass_method)
        backContactCost = getBackContactCost(backContact_method)
        absorberCost = getAbsorberCost(absorber_method)
        etlCost = getEtlCost(etl_method)

        formatted_total_cost = formatTotalCost(coverGlassCost, backContactCost, absorberCost, etlCost)
        
        # Create the bar chart
        fig = go.Figure()

        bar_title_font_style = dict(size=12, color="black", family=font_family)

        fig.add_trace(go.Bar(
            x=["Cover Glass"],
            y=[coverGlassCost],
            name="Cover Glass",
            marker=dict(color='red', line=dict(width=2, color="black")),
            text=[f"${coverGlassCost}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Back Contact"],
            y=[backContactCost],
            name="Back Contact",
            marker=dict(color='orange', line=dict(width=2, color="black")),
            text=[f"${backContactCost}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Absorber"],
            y=[absorberCost],
            name="Absorber",
            marker=dict(color='lightblue', line=dict(width=2, color="black")),
            text=[f"${absorberCost}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["ETL"],
            y=[etlCost],
            name="ETL",
            marker=dict(color='yellow', line=dict(width=2, color="black")),
            text=[f"${etlCost}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Total"],
            y=[formatted_total_cost],
            name="Total Cost",
            marker=dict(color='darkgreen', line=dict(width=2, color="black")),
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

        # Update graph layout
        fig.update_layout(
            title="Cost of Selected Methods",
            xaxis={
                'title': 'Method',
                'tickfont': dict(color="#afa732", family=font_family)  # Add this line
            },
            yaxis={
                'title': 'Cost', 
                'range': [0, 16], 
                'gridcolor': 'darkgray',
                'tickfont': dict(color="#afa732", family=font_family)  # Optional: match y-axis tick labels too
            },
            barmode='group',
            height=500,
            width=700,
            margin=dict(t=80, b=40, l=40, r=40),
            title_font=dict(size=24, color=font_color, family=font_family),
            xaxis_title_font=dict(size=18, color=font_color, family=font_family),
            yaxis_title_font=dict(size=18, color=font_color, family=font_family),
            legend=dict(font=dict(size=14, color=font_color, family=font_family)),
            paper_bgcolor=bg_color,
        )

        return fig
    
def update_revenue_graph(app):
    rev_data = revenueData()  

    @app.callback(
        Output('cost-revenue-chart', 'figure'),
        [
            Input('c-dropdown', 'value'),
            Input('b-dropdown', 'value'),
            Input('A-dropdown', 'value'),
            Input('e-dropdown', 'value')  
        ]
    )
    def update_graph(coverGlass_method, backContact_method, absorber_method, glass_method):

        
        coverGlassCost = rev_data.getCoverGlassRev(coverGlass_method)
        backContactCost = rev_data.getBackContactRev(backContact_method)
        absorberCost = rev_data.getAbsorberRev(absorber_method)
        glassCost = rev_data.getGlassRev(glass_method)

        # Calculate total cost
        formatted_total_cost = coverGlassCost + backContactCost + absorberCost + glassCost

        # Create the bar chart
        fig = go.Figure()

        bar_title_font_style = dict(size=12, color="black", family=font_family)

        fig.add_trace(go.Bar(
            x=["Cover Glass"],
            y=[coverGlassCost],
            name="Cover Glass",
            marker=dict(color='red', line=dict(width=2, color="black")),
            text=[f"${coverGlassCost:.2f}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Back Contact"],
            y=[backContactCost],
            name="Back Contact",
            marker=dict(color='orange', line=dict(width=2, color="black")),
            text=[f"${backContactCost:.2f}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Absorber"],
            y=[absorberCost],
            name="Absorber",
            marker=dict(color='lightblue', line=dict(width=2, color="black")),
            text=[f"${absorberCost:.2f}"],
            textposition="outside", 
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Glass"],
            y=[glassCost],
            name="Glass",
            marker=dict(color='yellow', line=dict(width=2, color="black")),
            text=[f"${glassCost:.2f}"],
            textposition="outside",  
            textfont=bar_title_font_style
        ))

        fig.add_trace(go.Bar(
            x=["Total"],
            y=[formatted_total_cost],
            name="Total Cost",
            marker=dict(color='darkgreen', line=dict(width=2, color="black")),
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
            title="Revenue of Selected Methods",
            xaxis={
                'title': 'Method',
                'tickfont': dict(color="#afa732", family=font_family)  # Add this line
            },
            yaxis={
                'title': 'Revenue', 
                'range': [0, 20], 
                'gridcolor': 'darkgray',
                'tickfont': dict(color="#afa732", family=font_family)  # Optional: match y-axis tick labels too
            },
            barmode='group',
            margin=dict(t=80, b=40, l=40, r=40),
            height=500,
            width=700,
            title_font=dict(size=24, color=font_color, family=font_family),
            xaxis_title_font=dict(size=18, color=font_color, family=font_family),
            yaxis_title_font=dict(size=18, color=font_color, family=font_family),
            legend=dict(font=dict(size=14, color=font_color, family=font_family)),
            paper_bgcolor=bg_color,
        )

        return fig