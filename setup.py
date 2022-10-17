from distutils.core import setup

setup(
    name="ais_trawler",
    url="https://github.com/aalling93/ais_trawler",
    author="Kristian Soerensen",
    author_email="kaaso@space.dtu.dk",
    install_requires=["numpy", "pandas", "bs4"],
    description="A web scraper to enrich AIS data with true metadata, such as length, widht, name etc. Name: Ais Trawler (pun intended).",
    long_description=open("README.md").read(),
)
