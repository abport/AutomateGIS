import pandas as pd
import fiona
from shapely.geometry import shape

# Set the directory where the shapefiles are located
shapefile_dir = '/path/to/shapefiles/'

# Create an empty list to store the merged shapefile
merged_shapes = []

# Iterate through the shapefiles in the directory
for shapefile in os.listdir(shapefile_dir):
    if shapefile.endswith('.shp'):
        # Open the shapefile using Fiona
        with fiona.open(shapefile_dir + shapefile) as f:
            # Iterate through the features in the shapefile
            for feature in f:
                # Convert the feature to a Shapely object
                feature_shape = shape(feature['geometry'])
                # Add the feature to the list of merged shapes
                merged_shapes.append(feature_shape)

# Create a new Shapefile using Fiona
with fiona.open('merged_shapefile.shp', 'w', driver='ESRI Shapefile', crs=f.crs, schema=f.schema) as f:
    # Iterate through the list of merged shapes
    for shape in merged_shapes:
        # Convert the Shapely shape back to a Fiona feature and write it to the Shapefile
        f.write({
            'geometry': shape.__geo_interface__,
            'properties': {}
        })

print('Shapefile merge complete!')
