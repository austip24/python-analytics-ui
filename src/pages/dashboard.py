"""Layout for the dashboard.

Variables:
    layout
"""

from dash import html, register_page
import dash_mantine_components as dmc
from src.utils.constants import ID_DASHBOARD_LINK
from src.components.figures import kpi, sample_area_chart

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
            [
                # dmc.Card(
                # [dmc.CardSection(className='bg-card text-card-foreground')], className='bg-card text-card-foreground border aspect-[16/7] col-span-1 row-span-1'),
                kpi(
                    title='Sales',
                    metric='$12,194',
                    metric_prev='$9,163',
                    delta=f'{(1-(9163/12194))*100:.2f}%'),
                kpi(
                    title='Profit',
                    metric='$40,598',
                    metric_prev='$45,564',
                    delta=f'{(1-(45564/40598))*100:.2f}%'),
                kpi(
                    title='Customers',
                    metric='1,072',
                    metric_prev='856',
                    delta=f'{(1-(856/1072))*100:.2f}%'),
                dmc.Card(
                    [dmc.CardSection([
                        html.Div(
                            html.H3('Sales for January Week 1',
                                    className='text-3xl font-bold px-6 pt-3 text-center')
                        ),
                        sample_area_chart], className='bg-card text-card-foreground h-full flex flex-col')], className='bg-card text-card-foreground border col-span-3 row-start-2 row-end-6')
            ],
            className='grid grid-cols-3 grid-rows-4 gap-8')
    ],
    className='grow flex flex-col gap-6 px-12 pb-10'
)
