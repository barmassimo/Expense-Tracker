"""
Support functions for Google App Engine
"""

import os


def runs_on_gae():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
        return True
    else:
        return False
