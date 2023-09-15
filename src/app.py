import dash
from dash import Dash, html

app = Dash(
    name=__name__,
    use_pages=True,
    title='Dash Test App',
    # assets_ignore='input.css'
    )

app.layout = html.Div(
    [
        html.Div([
            dash.page_container
        ])
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
