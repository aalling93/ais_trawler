# ais_trawler

A Web scraper made to enrich AIS data with extra information. Trawler, since we are *trawling* the internet for informaion on ships. Get it? hehe. 

When AIS data is transmitted, a IMU

Remeber, when scraping from the internet, you must abide by the robots.txt files.!

## From MMSI number to All data:

You can get data from two sources, giving different resutls. However, both returns length and width of the vessel. 


```python
with Trawler() as Tr:
    Tr.get_meta_v1(list_of_mmsi)

```


Returns:


|numer |imo|	mmsi	|length	|width	|type	|callsign	|Name|
| --- | --- | --- | --- | --- | --- | --- |--- |
|1	|9280689	| 205050000|	88|	13	|Cargo|	ONKX	|MARANT|
| --- | --- | --- | --- | --- | --- | --- |--- |
|2	|7802964	|205051000	|112	|18|	Dredger|	ORTV	|JAMES ENSOR|
| --- | --- | --- | --- | --- | --- | --- |--- |
|5	|9521461	|205085000	|90	|17	|Cargo|	ORUD|	SLOEBER|
| --- | --- | --- | --- | --- | --- | --- |--- |
|6	|9713478	|205087000	|199|	32|	Cargo	|ONMM	|CL EBISU|
| --- | --- | --- | --- | --- | --- | --- |--- |
