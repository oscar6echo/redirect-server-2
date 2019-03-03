
import os
import glob

import datetime as dt


class Util:
    """
    """

    def __init__(self):
        """
        """
        pass

    @staticmethod
    def get_time():
        """
        """
        return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_dist():
        """
        """
        here = os.path.dirname(__file__)
        root = os.path.join(here, '..')
        dist = os.path.normpath(os.path.join(root, 'vue', 'dist'))
        return dist
