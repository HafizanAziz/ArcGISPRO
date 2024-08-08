# Import the arcpy library, which provides access to ArcGIS tools and functionalities
import arcpy

# Import the env module from arcpy, which is used to set environment settings
from arcpy import env

# Import all functions from the arcpy.sa module, which provides access to spatial analyst tools
from arcpy.sa import *

# Set the workspace environment to the specified directory
env.workspace = "C:/path/to/your/workspace"

# Define the input feature class (shapefile) containing the replanting fields
input_fc = "replanting_fields.shp"

# Define the output feature class (shapefile) to store the rotated replanting fields
output_fc = "replanting_fields_rotated.shp"

# Define the rotation angle (in degrees) to be applied to the geometries
rotation_angle = 45

# Create a new feature class to store the rotated features, using the input feature class as a template
arcpy.CreateFeatureclass_management(out_path=env.workspace, out_name=output_fc, geometry_type="POLYGON", template=input_fc)

# Open a search cursor to iterate through each feature in the input feature class
with arcpy.da.SearchCursor(input_fc, ["SHAPE@"]) as search_cursor:
    # Open an insert cursor to add rotated features to the output feature class
    with arcpy.da.InsertCursor(output_fc, ["SHAPE@"]) as insert_cursor:
        # Iterate through each row (feature) in the input feature class
        for row in search_cursor:
            # Get the geometry of the current feature
            geometry = row[0]

            # Rotate the geometry by the specified angle
            rotated_geometry = geometry.rotate(rotation_angle)

            # Insert the rotated geometry into the output feature class
            insert_cursor.insertRow([rotated_geometry])

# Print a message indicating that the rotation is complete and specify the output location
print("Rotation complete. Output saved to:", output_fc)
