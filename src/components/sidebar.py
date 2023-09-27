"""Sidebar component with page links.

Function(s):
    create_sidebar_component
"""

from dash import Input, Output, State, callback, dcc, html, page_registry
from src.utils.constants import ID_LOCATION, ID_MAIN_CONTAINER, ID_SIDEBAR, ID_SIDEBAR_TOGGLE
import dash_mantine_components as dmc


# def create_sidebar_component() -> html.Div:
#     """Creates a sidebar component with page links for navigation

#     Page data is used to construct the sidebar's page links. A page is included
#     if 'sidebar=True' is added to the register_page() method (see .py files in /pages)

#     Returns:
#         html.Div: A sidebar with a link to each page
#     """

#     heading = dcc.Link(
#         [
#             html.Div(
#                 '<Placeholder>',
#                 className='text-center'
#             )
#         ],
#         href='/'
#     )

#     page_links = [
#         dcc.Link(
#             [
#                 html.Div(page['name'], className='')
#             ],
#             id=page['id_link'],
#             href=page['relative_path'],
#             className='hover:bg-muted hover:text-muted-foreground px-4 py-2 rounded transition-colors duration-150'
#         )
#         for page in page_registry.values()
#         if page.get('sidebar')
#     ]

#     return html.Div(
#         [
#             # dmc.Burger(id=ID_SIDEBAR_TOGGLE, opened=True,
#             #            size='md',
#             #            className='absolute top-2 -right-9 z-[100] bg-background text-foreground rounded cursor-pointer hover:bg-muted hover:text-muted-foreground transition-all duration-150 [&_*]:before:!bg-foreground [&_*]:after:!bg-foreground'),
#             dcc.Location(id=ID_LOCATION, refresh=False),
#             heading,
#             html.Div(
#                 page_links,
#                 className='flex flex-col gap-2'
#             )
#         ],
#         id=ID_SIDEBAR,
#         className="relative h-screen bg-background p-2 w-48 flex flex-col gap-4 border-r"
#         )

# TODO: Enable sidebar to be collapsible using this callback
# @callback(Output(ID_SIDEBAR, 'className'),
#           Output(ID_MAIN_CONTAINER, 'className'),
#           Input(ID_SIDEBAR_TOGGLE, 'opened')
#           )
# def toggle(opened):
#     if opened:
#         return "relative h-screen bg-background p-2 w-48 transition-spacing text-foreground flex flex-col gap-4 duration-200 border-r border-rose-500", "grow z-0 transition-transform translate-x-0"
#     else:
#         return "relative h-screen bg-background p-2 w-48 transition-spacing text-foreground flex flex-col gap-4 duration-200 border-r -ml-48 border-rose-500", "border grow z-0 transition-transform duration-200"


def create_sidebar_component() -> dmc.Navbar:
    return dmc.Navbar(
        children=[
            html.Div(
                [
                    html.H2('<Placeholder>',
                            className='text-xl font-bold text-center'),
                    # dmc.Divider(variant='solid', className='bg-rose-500'),
                    html.Div(
                        [

                            dmc.Anchor(
                                'Home', href='/', className='p-2 hover:bg-muted hover:text-muted-foreground transition-colors duration-200 rounded text-foreground bg-background hover:no-underline'),
                            dmc.Anchor(
                                'Dashboard', href='/dashboard', className='p-2 hover:bg-muted hover:text-muted-foreground transition-colors duration-200 rounded text-foreground bg-background hover:no-underline')
                        ],
                        className='flex flex-col gap-4 pt-4'
                    )
                ],
                className='flex flex-col gap-4 divide-y'
            )
        ],
        className='w-48 h-screen border-r p-4'
    )
