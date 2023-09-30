"""Layout for the dashboard.

Variables:
    layout
"""

from dash import html, register_page

from src.utils.constants import ID_DASHBOARD_LINK

register_page(
    __name__,
    sidebar=True,
    title='Dashboard',
    order=1,
    id_link=ID_DASHBOARD_LINK
)

layout = html.Div(
    [
        html.Div(
            'Dashboard', className="""py-2 flex justify-center font-semibold"""),
        html.Div([
            html.P('This is a placeholder dashboard.',
                   className='mb-4')
        ])
    ],
    className='h-full'
)
