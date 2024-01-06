from dash import html, dcc
import data_processing
import graphs

def create_layout():
    df_nombre_de_moi_count = data_processing.process_data()
    fig = graphs.create_bar_chart(df_nombre_de_moi_count)

    return html.Div([
        html.H1("Histogramme des Alternances par Plage de Durée"),
        dcc.Graph(figure=fig)
    ])
