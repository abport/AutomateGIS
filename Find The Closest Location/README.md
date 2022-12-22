This script uses the ArcGIS API for Python to find the closest location (e.g. store, hospital, school) to a given address or latitude/longitude coordinate.

First, you'll need to install the ArcGIS API for Python by running `pip install arcgis` in your command prompt or terminal.

Next, you'll need to create a free ArcGIS account and obtain a API key by following the instructions here: [https://developers.arcgis.com/python/guide/install-and-set-up/](https://developers.arcgis.com/python/guide/install-and-set-up/)

Once you have your API key, you can use the following script to find the closest location to a given point.

To use this script, simply replace `POINT` with the address or coordinates of the point you want to find the closest location to, `LOCATION_TYPE` with the type of location you want to find (e.g. hospital, school, store), and `DISTANCE` with the maximum distance you want to search (in miles). Then run the script using Python. The script will output the title of the closest location to the given point.

I hope this script is helpful for automating your GIS-related tasks! Let me know if you have any questions.
