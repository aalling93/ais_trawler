import multiprocessing

import numpy as np
import pandas as pd

from ._scrape import *


def mmsi_to_meta_parrallel_v1(mmsi_list: list):
    """and parrallelsing data."""

    agents = multiprocessing.cpu_count() - 1
    pool = multiprocessing.Pool(agents)
    result = pool.map(mmsi_to_data_marinevesseltraffic, mmsi_list)

    df = pd.DataFrame(
        np.array(result),
        columns=["imo", "mmsi", "length", "width", "type", "callsign", "Name"],
    )

    return df


def mmsi_to_meta_parrallel_v2(mmsi_list: list):
    """Threading and parrallelsing data."""

    agents = multiprocessing.cpu_count() - 1
    pool = multiprocessing.Pool(agents)
    result = pool.map(mmsi_to_data_myshiptracking, mmsi_list)

    df = pd.DataFrame(
        np.array(result),
        columns=[
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
        ],
    )

    return df
