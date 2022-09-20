from ._utilities import *
from ._get import *
from ._scrape import *


class Trawler:
    """ """

    def __init__(self):
        super(Trawler, self).__init__()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass

    def get_meta_v1(self, mmsi: list = []):
        """[imo, mmsi_online, length, width, type, callsign, name]"""

        self.df = mmsi_to_meta_parrallel_v1(mmsi)

    def get_meta_v2(self, mmsi: list = []):
        """[
            "imo",
            "mmsi",
            "length",
            "width",
            "type",
            "callsign",
            "name",
            "gross_tonnage",
            "deadweight_tonnage",
            "country",
        ]"""

        self.df = mmsi_to_meta_parrallel_v2(mmsi)
