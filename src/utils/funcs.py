"""Any helper functions should go in this file
"""

from dash_iconify import DashIconify


def get_icon(icon: str) -> DashIconify:
    return DashIconify(icon=icon, height=16)
