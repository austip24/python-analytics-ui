"""Layout for the home page

Variables:
    layout
"""

from dash import html, register_page

register_page(
    __name__,
    path='/'
)

layout = html.Div(
    html.Div(
        'Welcome to the Dash Test App',
        className='text-rose-500 text-center font-bold'
    )
)
