import arcpy, sys
import os
arcpy.env.overwriteOutput = True

workspace = r'C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb'
outWorkspace = r'C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb'

# Local variables:
targetFeatures = os.path.join(workspace, "Tracts")
joinFeatures = os.path.join(workspace, "General_Offense")

outfc = os.path.join(outWorkspace, "Join_General_Offense_and_Tracts")

#Run the Spatial Join tool, using the defaults for the join operation and join type
arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, outfc)



print ('Done')