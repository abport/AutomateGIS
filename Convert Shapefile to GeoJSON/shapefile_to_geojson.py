import os
import geopandas as gpd


def shapefiles_to_geojson(input_dir, output_dir):
    # Make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all the files in the input directory
    for file in os.listdir(input_dir):
        # Check if the file is a Shapefile
        if file.endswith('.shp'):
            # Read the Shapefile into a GeoDataFrame
            gdf = gpd.read_file(os.path.join(input_dir, file))
            # Convert the GeoDataFrame to a GeoJSON file
            gdf.to_file(os.path.join(output_dir, file.replace(
                '.shp', '.geojson')), driver='GeoJSON')


# Example usage
shapefiles_to_geojson('/path/to/input/directory', '/path/to/output/directory')
