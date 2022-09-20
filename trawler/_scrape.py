import numpy as np
import requests
from bs4 import BeautifulSoup
from ._utilities import *


def mmsi_to_data_myshiptracking(mmsi: int):
    """getting data from myshiptracking...
    You need a crawl delay of 5 for myshiptracking.com!
    """
    CRAWL_DELAY = 5
    site = f"https://www.myshiptracking.com/vessels/mmsi-{mmsi}"
    try:
        time_delay(CRAWL_DELAY)
        page = requests.get(site)
    except:
        print(f"Connection refused by the server.. Sleeping for 5 sec")
        time_delay(CRAWL_DELAY+2)
        pass

    soup = BeautifulSoup(page.content, "html.parser")

    soup.select("vsl-info-card ")
    soup.select("table")
    soup.select("tbody")

    try:
        imo = int(soup.select("tr:nth-child(2)")[0].text.strip().split("\n")[1])
    except:
        imo = -1
    try:
        mmsi_online = int(soup.select("tr:nth-child(3)")[0].text.strip().split("\n")[1])
    except:
        # self.missing_mmsi.append(mmsi)
        mmsi_online = -1

    try:
        country = soup.select("tr:nth-child(4)")[0].text.strip().split("\n")[1].strip()
    except:
        country = -1

    try:
        length = float(
            soup.select("tr:nth-child(6)")[0]
            .text.strip()
            .split("\n")[1]
            .split("x")[0]
            .strip()
        )
    except:
        length = -1
    try:
        width = float(
            soup.select("tr:nth-child(6)")[0]
            .text.strip()
            .split("\n")[1]
            .split("x")[1]
            .strip()
            .split(" ")[0]
            .strip()
        )
    except:
        width = -1
    try:
        type = soup.select("td.vessel_td.td_type")[0].text.strip()
    except:
        type = -1
    try:
        callsign = soup.select("tr:nth-child(5)")[0].text.strip().split("\n")[1]
    except:
        callsign = -1

    try:
        gross_tonnage = float(
            soup.select("tr:nth-child(7)")[0].text.strip().split("\n")[1].split(" ")[0]
        )
    except:
        gross_tonnage = -1

    try:
        deadweight_tonnage = float(
            soup.select("tr:nth-child(8)")[0].text.strip().split("\n")[1].split(" ")[0]
        )
    except:
        deadweight_tonnage = -1
    # country = soup.select('td:nth-child(1).vessel_td')[0]
    try:
        soup = BeautifulSoup(page.content, "html.parser")
        soup.select("stick-id-1")
        soup.select("div")
        soup.select("div")
        soup.select("div")
        soup.select(
            "div.d-flex.p-2.text-center.text-sm-left.flex-grow-1.justify-center-sm"
        )
        soup.select("div")
        soup.select("div:nth-child(1)")
        name = soup.select("h1")[0].text
    except:
        name = -1

    return np.array(
        [
            imo,
            mmsi_online,
            length,
            width,
            type,
            callsign,
            name,
            gross_tonnage,
            deadweight_tonnage,
            country,
        ]
    )


def mmsi_to_data_marinevesseltraffic(mmsi: int):
    """getting data from marinevesseltraffic.."""
    CRAWL_DELAY = 5
    site = f"https://www.marinevesseltraffic.com/vessels?page=1&vessel={mmsi}&sort=none&direction=none&flag=none"
    try:
        time_delay(CRAWL_DELAY)
        page = requests.get(site)
    except:
        print(f"Connection refused by the server.. Sleeping for 5 sec")
        time_delay(CRAWL_DELAY)
        pass

    soup = BeautifulSoup(page.content, "html.parser")

    soup.select("body")
    soup.select("div.container")
    soup.select("div.col-s-12.col-m-9.col-l-10")
    soup.select("div:nth-child(4)")
    soup.select("div")
    soup.select("table")
    soup.select("tbody")
    soup.select("tr.vessel_row")

    try:
        imo = int(soup.select("td.vessel_td.td_imo")[0].text.strip())
    except:
        imo = -1
    try:
        mmsi_online = int(soup.select("td.vessel_td.td_mmsi")[0].text.strip())
    except:
        mmsi_online = -1

    try:
        length = int(soup.select("td.vessel_td.td_length")[0].text.strip())
    except:
        length = -1
    try:
        width = int(soup.select("td.vessel_td.td_beam")[0].text.strip())
    except:
        width = -1
    try:
        type = soup.select("td.vessel_td.td_type")[0].text.strip()
    except:
        type = -1
    try:
        callsign = soup.select("td.vessel_td.td_call_sign")[0].text.strip()
    except:
        callsign = -1
    try:
        name = soup.select("td:nth-child(4).vessel_td")[0].text.strip()
    except:
        name = -1

    return np.array([imo, mmsi_online, length, width, type, callsign, name])
