from dash import html, dcc
import data_processing
import graphs

def create_layout():
    # Process data using the 'process_data' function from the 'data_processing' module
    df_nombre_de_moi_count = data_processing.process_data()

    # Create a bar chart using the processed data
    fig = graphs.create_bar_chart(df_nombre_de_moi_count)

    # Define the layout of the page
    return html.Div([
        # Add a centered header to the page
        html.H1("Histogramme des Alternances par Plage de Durée", style={'textAlign': 'center'}),

        # Create a container for the graph
        html.Div(
            dcc.Graph(figure=fig),
            # Style the container for center alignment
            style={'display': 'flex', 'justifyContent': 'center'}
        )
    ])
