import geojson
from arcgis.gis import GIS
from arcgis.geometry import Geometry

# Replace YOUR_API_KEY with your actual API key
gis = GIS("https://www.arcgis.com", api_key="YOUR_API_KEY")

# Replace POINT_1 and POINT_2 with the coordinates or addresses of the two points you want to find the route between
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

# Find the shortest route between the points
route_result = gis.network.route(
    point_1, point_2, return_routes=True, return_directions=True)
route = route_result['routes']['features'][0]

# Convert the route to a GeoJSON feature
geojson_feature = geojson.Feature(
    geometry=route['geometry'], properties=route['attributes'])

# Save the GeoJSON feature to a file
with open('route.geojson', 'w') as f:
    geojson.dump(geojson_feature, f)

print('Route saved to route.geojson')
