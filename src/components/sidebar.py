"""Sidebar component with page links.

Function(s):
    create_sidebar_component
"""

from dash import Input, Output, State, callback, dcc, html, page_registry
from utils.constants import ID_LOCATION
from utils.funcs import update_utility_classes


def create_sidebar_component() -> html.Div:
    """Creates a sidebar component with page links for navigation

    Page data is used to construct the sidebar's page links. A page is included
    if 'sidebar=True' is added to the register_page() method (see .py files in /pages)

    Returns:
        html.Div: A sidebar with a link to each page
    """

    heading = dcc.Link(
        [
            html.Div(
                '<Logo Icon>',
                className='text-center'
            )
        ],
        href='/'
    )

    page_links = [
        dcc.Link(
            [
                html.Div(page['name'], className='')
            ],
            id=page['id_link'],
            href=page['relative_path'],
            className=''
        )
        for page in page_registry.values()
        if page.get('sidebar')
    ]

    return html.Div(
        [
            dcc.Location(id=ID_LOCATION, refresh=False),
            heading,
            html.Div(
                [*page_links],
                className='flex flex-col gap-2'
            )
        ],
        className='h-screen bg-slate-800 p-2 w-32 fixed overflow-auto text-slate-50 flex flex-col gap-4')
