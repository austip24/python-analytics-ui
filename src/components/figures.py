"""Key Performance Indicator Component

Function(s):
    kpi
    bar_chart
"""

from typing import Optional
from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from src.data.process_data import sample_data
import plotly.express as px

from src.utils.constants import ID_SAMPLE_PLOT


def kpi(title: str,
        metric: str,
        metric_prev: Optional[str] = None,
        delta: Optional[str] = None) -> dmc.Card:

    delta_as_numeric = float(delta.replace('%', ''))

    increased = delta_as_numeric > 0

    return dmc.Card(
        [
            dmc.CardSection(
                [
                    html.Div(
                        [
                            html.H3(title, className='text-muted-foreground'),
                            html.Div(
                                [
                                    dmc.Badge(
                                        [
                                            # render icon based on condition
                                            DashIconify(icon='lucide:arrow-up-right', className='w-4 h-4') if increased
                                            else DashIconify(icon='lucide:arrow-down-right', className='w-4 h-4'),

                                            # delta value
                                            html.P(delta.replace('-', '')),
                                        ],
                                        className=f'{"bg-emerald-100 text-emerald-700" if delta_as_numeric > 0 else "bg-rose-100 text-rose-700"} font-medium px-2 py-2.5 text-sm [&>.mantine-Badge-inner]:flex [&>.mantine-Badge-inner]:items-center [&>.mantine-Badge-inner]:gap-1'),
                                ]
                            ),
                        ],
                        className='flex items-center justify-between'
                    ),
                    html.Div(
                        [
                            html.Div(
                                metric, className='text-card-foreground text-3xl font-bold'),
                            html.Div(
                                [
                                    html.Span(
                                        f'from {metric_prev}', className='truncate'),
                                ]
                            )
                        ],
                        className='text-muted-foreground flex gap-2 items-end'
                    )
                ],
                className='p-6 flex flex-col gap-1'
            )
        ],
        className='bg-card text-card-foreground border rounded-lg w-full min-w-[300px]',
    )


# TODO: make this an area chart instead of a line chart
area_chart = px.line(
    data_frame=sample_data,
    x='Dates',
    y='Sales',
    markers=True,
)

area_chart.update_layout(
    xaxis={
        "showgrid": False
    },
    yaxis={
        "showgrid": False
    },
    margin=dict(l=0, r=0, t=0, b=0),
    showlegend=False,
)

sample_area_chart = dcc.Graph(
    figure=area_chart,
    # figure={
    #     "data": [{
    #         "x": sample_data['Dates'],
    #         "y": sample_data['Sales'],
    #         'type': 'area'
    #     }]
    # },
    id=ID_SAMPLE_PLOT,
    config={
        'displayModeBar': False,
    },
    responsive=True,
    className='h-full w-full [&_.bglayer>rect]:!fill-background [&_.main-svg:nth-child(1)]:!bg-background [&_.main-svg_.zerolinelayer>path]:!stroke-accent [&_text]:!fill-secondary-foreground px-6 [&_.plot_.fills_.js-fill]:!fill-[linear-gradient(to bottom, red, blue)]'
)
