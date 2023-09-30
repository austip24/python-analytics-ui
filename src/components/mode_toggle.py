"""Dark Mode Toggle Button

Function(s):
    mode_toggle
"""


from dash_iconify import DashIconify
from dash import callback, html, Input, Output, State

from src.utils.constants import ID_APP_CONTAINER, ID_THEME_BUTTON


def mode_toggle() -> html.Button:
    return html.Button(
        id=ID_THEME_BUTTON,
        className='border p-2 rounded bg-background hover:bg-muted',
        n_clicks=0,
    )


@callback(Output(ID_APP_CONTAINER, 'className'),
          Output(ID_THEME_BUTTON, 'children'),
          State(ID_APP_CONTAINER, 'className'),
          Input(ID_THEME_BUTTON, 'n_clicks'))
def toggle_theme(className, n_clicks):
    print(f'{n_clicks = }')
    if n_clicks % 2 == 0:
        return [f'{className.replace("dark", "")} dark', DashIconify(icon='bi:sun', width=24)]
    return [f'{className.replace("dark", "")}', DashIconify(icon='bi:moon', width=24)]
