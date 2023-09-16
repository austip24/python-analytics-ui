import dash
from dash import Dash, html

from components.sidebar import create_sidebar_component


def main() -> None:
    app = Dash(
        name=__name__,
        use_pages=True,
        title='Dash app',
        assets_ignore='input.css',
        extra_hot_reload_paths=['./src/assets/css/dist/output.css']
    )

    app.layout = html.Div(
        [
            create_sidebar_component(),
            html.Div([
                dash.page_container
            ], className='grow ml-32 h-auto')
        ],
        className='flex'
    )

    app.run(debug=True, dev_tools_hot_reload=True, threaded=True)


if __name__ == '__main__':
    main()
