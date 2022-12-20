# This script copies a feature class of points and adds some new fields to it. It also projects the points to a different coordinate system.

# First, we need to import a library called arcpy that has special tools for working with GIS data.
import arcpy

# Next, we need to tell the script which feature class we want to copy (the input feature class) and where we want to save the copy (the output feature class).
in_fc = "input_points.shp"  # This is the feature class we want to copy.
out_fc = "output_points.shp"  # This is where we want to save the copy of the feature class.

# We also need to tell the script which coordinate system we want to use for the output feature class. This is called the spatial reference.
sr = arcpy.SpatialReference(4326)  # We want to use the WGS 84 coordinate system.

# Now we can use a tool from the arcpy library to create an empty feature class with the same schema as the input feature class.
arcpy.CreateFeatureclass_management(out_fc, "POINT", spatial_reference=sr)  # This creates an empty feature class called "output_points.shp" with a point geometry type and the WGS 84 coordinate system.

# We also want to add some new fields to the output feature class.
arcpy.AddField_management(out_fc, "ID", "LONG")  # This adds a field called "ID" to the output feature class. It will be used to store a number.
arcpy.AddField_management(out_fc, "NAME", "TEXT", field_length=50)  # This adds a field called "NAME" to the output feature class. It will be used to store some text, and it can be up to 50 characters long.

# Now we can copy the data from the input feature class to the output feature class. To do this, we need to open a cursor to each feature class.
with arcpy.da.SearchCursor(in_fc, ["OID@", "NAME"]) as in_cursor, arcpy.da.InsertCursor(out_fc, ["ID", "NAME"]) as out_cursor:
    # A cursor is like a pointer that we can use to read through the rows of a feature class.
    # The "with" statement is used to make sure that the cursors are closed properly when we're done.
    
    # Now we can loop through the rows of the input cursor.
    for row in in_cursor:
        # For each row, we can get the values of the OID and NAME fields.
        oid = row[0]  # The OID field contains a unique number for each row.
        name = row[1]  # The NAME field contains some text.
        
        # Now we can insert a new row into the output cursor with the ID and NAME values.
        out_cursor.insertRow((oid, name))  # This inserts a new row into the output feature class with the ID and NAME values from the input feature class.

# Finally, we can use another tool from the arcpy library to project the output feature class to a different coordinate system.
arcpy.Project_management(out_fc, "output_points_projected.shp", sr)  # This projects the output feature class to the WGS 84 coordinate system and saves it as a new feature class called "output_points_projected.shp".

