from dash import Dash, html

app = Dash(
    name=__name__,
    use_pages=True,
    title='Dash Test App',
    assets_ignore='input.css')

server = app.server

# app.layout = html.Div(
#     [
#         # Sidebar
#         create_sidebar_component(),
#         # Main content
#         html.Div([
#             dash.page_container,
#             footer_component
#         ],
#                  className='lm-32 ')
#     ]
# )

if __name__ == '__main__':
    app.run(debug=True)
