"""Page header bar

Function(s):
    header
"""

from dash import html

from src.components.mode_toggle import mode_toggle


def header() -> html.Header:
    return html.Header(
        [
            mode_toggle()
        ],
        className='z-10 p-2 h-16 fixed top-0 left-0 right-0 border-b flex items-center justify-end'
    )
