from distutils.core import setup

setup(
  name='trawler',
  url='coming',
  author='Kristian Soerensen',
  author_email='kaaso@space.dtu.dk',
  packages=['trawler',],
  install_requires=['numpy', 'pandas','bs4'],
  version='0.1',
  license='MIT',
  description='A web scraper to enrich AIS data with true metadata, such as length, widht, name etc. Name: Trawler (pun intended).',
  long_description=open('README.md').read()
)