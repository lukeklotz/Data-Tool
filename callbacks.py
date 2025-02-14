from dash import Output, Input
from costGraph import create_bar_chart


def register_callbacks(app, coverGlass, backContact, Absorber, etl, font_family, font_color, bg_color):
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
        return create_bar_chart(coverGlass, backContact, Absorber, etl, font_family, font_color, bg_color)