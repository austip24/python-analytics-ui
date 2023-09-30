"""Layout for the home page

Variables:
    layout
"""

from src.components.mode_toggle import mode_toggle
from dash import html, register_page

from src.utils.constants import ID_HOME_LINK

register_page(
    __name__,
    path='/',
    title='Home',
    sidebar=True,
    order=0,
    id_link=ID_HOME_LINK,
)

layout = html.Div(
    [
        # mode_toggle(),
        html.Div(
            'Welcome to the App',
            className='font-bold text-5xl pb-40 xl:text-6xl'
        ),
    ],
    className='flex h-full items-center justify-center'
)
