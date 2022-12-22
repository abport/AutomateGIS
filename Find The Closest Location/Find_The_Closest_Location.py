from arcgis.gis import GIS
from arcgis.geocoding import geocode

# Replace YOUR_API_KEY with your actual API key
gis = GIS("https://www.arcgis.com", api_key="YOUR_API_KEY")

# Replace POINT with the address or coordinates of the point you want to find the closest location to
point = POINT

# Geocode the point if it is an address
if isinstance(point, str):
    point = geocode(point)[0]['location']

# Replace LOCATION_TYPE with the type of location you want to find (e.g. hospital, school, store)
# Replace DISTANCE with the maximum distance you want to search (in miles)
locations = gis.content.search(query=f"{LOCATION_TYPE} AND distance(location, {point}) < {DISTANCE}",
                               outside_org=True, max_items=1)

if locations:
    closest_location = locations[0]
    print(f'The closest {LOCATION_TYPE} is {closest_location.title}')
else:
    print(f'No {LOCATION_TYPE} found within {DISTANCE} miles')
