import dash
from dash import Dash, html
from src.components.sidebar import create_sidebar_component

from src.utils.constants import ID_MAIN_CONTAINER


def main() -> None:
    app = Dash(
        name=__name__,
        use_pages=True,
        pages_folder='./src/pages',
        assets_folder='./src/assets',
        title='Dash app',
        assets_ignore='input.css',
    )

    app.layout = html.Div(
        [
            create_sidebar_component(),
            html.Div([
                dash.page_container
            ],
                id=ID_MAIN_CONTAINER,
                className='grow z-0 px-12'
                )
        ],
        className='relative flex w-full h-screen overflow-hidden'
    )

    app.run(debug=True, reloader_interval=1, threaded=True)


if __name__ == '__main__':
    main()
