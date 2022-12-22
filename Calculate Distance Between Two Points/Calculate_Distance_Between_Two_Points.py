from arcgis.geometry import Geometry
from arcgis.gis import GIS

# Replace YOUR_API_KEY with your actual API key
gis = GIS("https://www.arcgis.com", api_key="YOUR_API_KEY")

# Replace POINT_1 and POINT_2 with the coordinates or addresses of the two points you want to measure
point_1 = POINT_1
point_2 = POINT_2

# Geocode the points if they are addresses
if isinstance(point_1, str):
    point_1 = gis.geocoder.geocode(point_1)[0]['location']
if isinstance(point_2, str):
    point_2 = gis.geocoder.geocode(point_2)[0]['location']

# Convert the points to ArcGIS geometry objects
point_1 = Geometry(point_1)
point_2 = Geometry(point_2)

# Calculate the distance between the points
distance = point_1.distance(point_2)

# Print the distance in miles
print(f'Distance: {distance} miles')
