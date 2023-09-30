"""Layout for the dashboard.

Variables:
    layout
"""

from dash import html, register_page
import dash_mantine_components as dmc
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
            'Dashboard', className="""pt-4 flex justify-center font-semibold"""),
        html.Div(
            [dmc.Card(
                [dmc.CardSection(className='bg-card text-card-foreground')], className='bg-card text-card-foreground border aspect-[16/7] col-span-1 row-span-1'),
             dmc.Card(
                [dmc.CardSection(className='bg-card text-card-foreground')], className='bg-card text-card-foreground border aspect-[16/7] col-span-1 row-span-1'),
             dmc.Card(
                [dmc.CardSection(className='bg-card text-card-foreground')], className='bg-card text-card-foreground border aspect-[16/7] col-span-1 row-span-1'),
             dmc.Card(
                [dmc.CardSection(className='bg-card text-card-foreground')], className='bg-card text-card-foreground border col-span-3 row-span-2')
             ],
            className='grid grid-cols-3 grid-rows-3 gap-8')
    ],
    className='grow flex flex-col gap-8 px-12 pb-10'
)
