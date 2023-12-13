import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go

# Function to get dimensions from the API
def get_dimensions(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Update the path to navigate the JSON response correctly
        dimensions = data.get('components', {}).get('schemas', {}).get('MetierEnrichi', {}).get('romes', [])

        if not dimensions:
            print("No dimensions found in the API response.")
            return []
        return dimensions
    except Exception as e:
        print(f"Error fetching dimensions: {str(e)}")
        return []

# Function to get data for a specific dimension
def get_data_for_dimension(api_url, dimension_code):
    try:
        response = requests.get(f"{api_url}/{dimension_code}")
        response.raise_for_status()
        data = response.json()

        # Update this block based on the actual structure of the API response
        if 'romes' in data:
            return data['romes']
        else:
            print(f"Key 'romes' not found in data for dimension {dimension_code}.")
            return []
    except Exception as e:
        print(f"Error fetching data for dimension {dimension_code}: {str(e)}")
        return []

# Dash app configuration
app = dash.Dash(__name__)

# API URL
api_url = "https://labonnealternance.apprentissage.beta.gouv.fr/api"  # Update with the correct API endpoint
dimensions = get_dimensions(api_url)

# Dashboard layout
app.layout = html.Div([
    html.H1("Alternance API Dashboard"),

    html.Label("Select a dimension:"),
    dcc.Dropdown(
        id='dimension-dropdown',
        # Update 'label' and 'value' with the keys present in your dimensions data
        options=[{'label': dimension['label'], 'value': dimension['codeRome']} for dimension in dimensions],
        value=dimensions[0]['codeRome'] if dimensions else None
    ),

    dcc.Graph(id='dimension-graph'),

    html.Div(id='selected-dimension'),
])

# Callback to update the display based on the selected dimension
@app.callback(
    [Output('selected-dimension', 'children'),
     Output('dimension-graph', 'figure')],
    [Input('dimension-dropdown', 'value')]
)
def update_selected_dimension(selected_dimension):
    data = get_data_for_dimension(api_url, selected_dimension)

    # Update 'x' and 'y' data extraction according to your data structure
    x_data = [entry.get('YourXKey', 0) for entry in data]
    y_data = [entry.get('YourYKey', 0) for entry in data]

    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode='lines+markers',
        name='Dimension Curve'
    )

    layout = go.Layout(
        title=f"Dimension Curve for {selected_dimension}",
        xaxis=dict(title='X-Axis'),
        yaxis=dict(title='Y-Axis')
    )

    return f"You have selected the dimension: {selected_dimension}", {'data': [trace], 'layout': layout}

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
