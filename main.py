import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, callback

# Create Dash app
app = dash.Dash(__name__)

# Load data
data = pd.read_excel("DATA_EMMA.xlsx", sheet_name=11)

# Filter relevant columns
filtered_data = data[["Unnamed: 14", "Method", "Cost"]]

# Extract the unique labels
labels = filtered_data["Unnamed: 14"].dropna().unique()

# Group Data
coverGlass = filtered_data.iloc[0:3] #.iloc[num:num] extracts corresponding data
backContact = filtered_data.iloc[3:6]
Absorber = filtered_data.iloc[6:10]
etl = filtered_data.iloc[10:11]

# Get list of methods from each group
coverGlass_methods = coverGlass["Method"].tolist()
backContact_methods = backContact["Method"].tolist()
Absorber_methods = Absorber["Method"].tolist()
etl_methods = etl["Method"].tolist()


#drop down and background styles
width = '70%'
dd_color = '#353431'
bg_color = '#23221B'
background_color = '#8E9FA3'

#bar graph styles
font_color = "#afa732"
font_family = "Courier New"

app.layout = html.Div([
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
        ], style={'width': '50%', 'padding-left': '30px', 
                  'display': 'flex', 'justify-content': 'center', 
                  'align-items': 'center',
                  'background': dd_color,
                  'color': font_color}),  # Flexbox to center the graph
    ], style={'background': dd_color, 'display': 'flex', 
              'align-items': 'flex-start', 
              'justify-content': 'center', 
              'width': '90%',
              'border-radius': '15px',
              'border': 'solid black 2px',
              'padding': '25px'}),  # Flexbox layout to align side by side and center horizontally
], style={'display': 'flex', 'flex-direction': 'column', 
          'align-items': 'center', 'justify-content': 'center', 
          'height': '100vh',
          'background': bg_color,
          'padding': '0',
          'margin': '0',
          })  # Outer Div to center everything on the page


# Function to generate the bar chart based on selected methods
@app.callback(
    Output('cost-bar-chart', 'figure'),
    [
        Input('coverGlass-dropdown', 'value'),
        Input('backContact-dropdown', 'value'),
        Input('Absorber-dropdown', 'value'),
        Input('etl-dropdown', 'value')
    ]
)

def update_graph(coverGlass_method, backContact_method, Absorber_method, etl_method):
    # Get the selected rows based on the method
    coverGlass_row = coverGlass[coverGlass["Method"] == coverGlass_method]
    backContact_row = backContact[backContact["Method"] == backContact_method]
    Absorber_row = Absorber[Absorber["Method"] == Absorber_method]
    etl_row = etl[etl["Method"] == etl_method]

    # Extract the costs
    coverGlass_cost = coverGlass_row["Cost"].values[0]
    backContact_cost = backContact_row["Cost"].values[0]
    Absorber_cost = Absorber_row["Cost"].values[0]
    etl_cost = etl_row["Cost"].values[0]

    total_cost = coverGlass_cost + backContact_cost + Absorber_cost + etl_cost
    formatted_total_cost = round(total_cost, 2)
    
    # Create the bar chart
    fig = go.Figure()

    bar_title_font_style = dict(size=12, color="black", family=font_family)
    # Add each selected item to the bar chart with customized colors
    # Add each selected item to the bar chart with customized colors
    fig.add_trace(go.Bar(
        x=["Cover Glass"],
        y=[coverGlass_row["Cost"].values[0]],
        name="Cover Glass",
        marker=dict(color='lightblue'),  # Customize color
        text=[f"${coverGlass_row['Cost'].values[0]}"],  # The text label for the bar
        textposition="outside",  # Position of the text (outside the bar)
        textfont=bar_title_font_style  # Apply custom font style
    ))

    fig.add_trace(go.Bar(
        x=["Back Contact"],
        y=[backContact_row["Cost"].values[0]],
        name="Back Contact",
        marker=dict(color='lightgreen'),  # Customize color
        text=[f"${backContact_row['Cost'].values[0]}"],  # The text label for the bar
        textposition="outside",  # Position of the text (outside the bar)
        textfont=bar_title_font_style,  # Apply custom font style
    ))

    fig.add_trace(go.Bar(
        x=["Absorber"],
        y=[Absorber_row["Cost"].values[0]],
        name="Absorber",
        marker=dict(color='lightcoral'),  # Customize color
        text=[f"${Absorber_row['Cost'].values[0]}"],  # The text label for the bar
        textposition="outside",  # Position of the text (outside the bar)
        textfont=bar_title_font_style,  # Apply custom font style
    ))

    fig.add_trace(go.Bar(
        x=["ETL"],
        y=[etl_row["Cost"].values[0]],
        name="ETL",
        marker=dict(color='gold'),  # Customize color
        text=[f"${etl_row['Cost'].values[0]}"],  # The text label for the bar
        textposition="outside",  # Position of the text (outside the bar)
        textfont=bar_title_font_style  # Apply custom font style
    ))

     # Add annotation for the total cost
    fig.add_annotation(
        text=f"Total Cost: ${formatted_total_cost}",
        xref="paper", yref="paper",
        x=1.29, y=0.0,
        showarrow=False,
        font=dict(size=16, color=font_color, family=font_family),
        align="center"
    )

    # Update layout with increased height, font size, and grid lines
    fig.update_layout(
        title="Cost of Selected Methods",
        xaxis={'title': 'Category'},
        yaxis={
            'title': 'Cost',
            'range': [0, 10],  # Adjust y-axis range for smaller prices
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
            'width': 2
        }
    }]
    )
    
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
