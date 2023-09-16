"""Layout for the home page

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import ID_HOME_LINK

register_page(
    __name__,
    path='/',
    sidebar=True,
    order=0,
    id_link=ID_HOME_LINK,
)

layout = html.Div(
    [
        html.Div(
            'Welcome to the App',
            className='font-bold text-5xl pb-40 text-slate-700 x:text-6xl'
        ),
    ],
    className='flex h-full items-center justify-center'
)
