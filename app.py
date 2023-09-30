import dash
from dash import Dash, html
from src.components.header import header
from src.components.sidebar import sidebar

from src.utils.constants import ID_APP_CONTAINER, ID_MAIN_CONTAINER


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
            sidebar(),
            html.Div([
                header(),
                html.Div(
                    [
                        dash.page_container
                    ],
                    className='pt-16 grow flex flex-col'
                )
            ],
                id=ID_MAIN_CONTAINER,
                className='w-full z-0 flex flex-col'
            )
        ],
        className='relative flex min-h-screen w-full bg-background text-foreground',
        id=ID_APP_CONTAINER
    )

    app.run(debug=True, reloader_interval=1, threaded=True)


if __name__ == '__main__':
    main()
