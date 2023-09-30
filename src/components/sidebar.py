"""Sidebar component with page links.

Function(s):
    sidebar
"""

from dash import Input, Output, State, callback, dcc, html, page_registry
from src.utils.constants import ID_DASHBOARD_LINK, ID_HOME_LINK, ID_LOCATION
import dash_mantine_components as dmc


def sidebar() -> dmc.Navbar:
    # for link in page_links:
    #     print(link)
    page_links = [
        dmc.NavLink(
            label=page['title'].capitalize(),
            id=page['id_link'],
            href=page['relative_path'],
            className='p-2 hover:bg-muted hover:text-muted-foreground transition-colors duration-200 rounded text-foreground bg-background hover:no-underline [&_.mantine-NavLink-label]:text-base'
        ) for page in page_registry.values() if page.get('sidebar')
    ]

    return dmc.Navbar(
        children=[
            dcc.Location(id=ID_LOCATION, refresh=False),
            html.Div(
                [
                    html.H2('<Placeholder>',
                            className='text-xl font-bold text-center'),
                    html.Div(
                        [*page_links],
                        className='flex flex-col gap-4 pt-4'
                    )
                ],
                className='flex flex-col gap-4 divide-y'
            )
        ],
        className='z-20 w-48 sticky top-0 bottom-0 border-r border-border p-4 bg-background text-foreground'
    )


# @callback(
#     output={
#         link['href']: link['className'] for link in page_links
#         # x: y for page in page_links
#         # "home_className": Output(ID_HOME_LINK, 'className'),
#         # "dashboard_className": Output(ID_DASHBOARD_LINK, 'className')
#     },
#     inputs={
#         "pathname": Input(ID_LOCATION, 'pathname'),
#         "home_link": {
#             "className": State(ID_HOME_LINK, 'className'),
#             "href": State(ID_HOME_LINK, 'href')
#         },
#         "dashboard_link": {
#             "className": State(ID_DASHBOARD_LINK, 'className'),
#             "href": State(ID_DASHBOARD_LINK, 'href')
#         },
#     }
# )
# def indicate_current_page(pathname, home_link, dashboard_link):
#     active_class = 'p-2 transition-colors duration-200 rounded text-primary-foreground bg-primary hover:no-underline'
#     print(f'{pathname = }')
#     print(f'{home_link["href"] = }')
#     print(f'{dashboard_link["href"] = }')
#     if pathname == home_link['href']:
#         return {
#             "home_className": active_class,
#             "dashboard_className": dashboard_link['className']
#         }
#     elif pathname == dashboard_link['href']:
#         return {
#             "home_className": active_class,
#             "dashboard_className": dashboard_link['className']
#         }
