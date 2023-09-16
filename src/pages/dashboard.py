"""Layout for the dashboard.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import ID_DASHBOARD_LINK

register_page(
    __name__,
    sidebar=True,
    order=1,
    id_link=ID_DASHBOARD_LINK
)

layout = html.Div(
    [
        html.Div(
            'Dashboard', className="""py-2 flex justify-center bg-slate-700 text-emerald-50 font-semibold"""),
        html.Div([
            html.P('This is a placeholder dashboard.',
                   className='mb-4 text-inherit')
        ])
    ],
    className='min-h-screen'
)
