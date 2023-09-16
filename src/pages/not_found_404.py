"""Layout when user navigates to a route that doesn't exist.

Variables:
    layout
"""

from dash import html, register_page

register_page(__name__)

layout = html.Div(
    [
        html.H1(
            '404',
            className='text-center font-extrabold text-6xl'
        ),
        html.Div(
            """This page does not exist. Please use the page links in the sidebar to
        navigate the website.""",
            className="text-lg",
        ),
    ],
    className="flex flex-col gap-8 items-center justify-center h-screen text-slate-700",
)
