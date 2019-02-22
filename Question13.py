import arcpy
arcpy.env.overwriteOutput = True




#-----------------------------------------------
# Creating New GDB
GDBLocation = r'C:\Users\ralnefai\Desktop\GIS610\Question 13'
GDBName = 'Question13'

arcpy.CreateFileGDB_management (GDBLocation, GDBName)

print ('Your GDB been Created')
#-----------------------------------------------


#-----------------------------------------------
# Import all of the shape files in the folder to the new geodatabase
# Set local variables
Features = [r"C:\Users\ralnefai\Desktop\GIS610\Question 13\tl_2018_04_tract.shp", r"C:\Users\ralnefai\Desktop\GIS610\Question 13\tl_2018_us_county.shp"]
GDB = r'C:\Users\ralnefai\Desktop\GIS610\Question 13\Question13.gdb'
out_location = GDB
 
# Execute FeatureClassToGeodatabase
arcpy.FeatureClassToGeodatabase_conversion(Features, out_location)

print ('Features imported to the GDB')
#-----------------------------------------------

# sitting the work space for the upcoming steps 
arcpy.env.workspace = GDB

#-----------------------------------------------
# Extracting Maricopa County 
inFeatures = 'tl_2018_us_county'
outLocation = GDB
outFeatureClass = "MaricopaCounty"
delimitedField = arcpy.AddFieldDelimiters(inFeatures, "Name")
expression = delimitedField + " = 'Maricopa'"
 
# Execute FeatureClassToFeatureClass to create a new feature class based on call for service type 'Family Fight Call'
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, expression)
print ('Maricopa County feature class created')
#-----------------------------------------------



#-----------------------------------------------
# Performing Clip function to clip Tracts within Maricopa 
# Set local variables
tagetFeatcherClass = 'tl_2018_04_tract'
clip_features = 'MaricopaCounty'
out_feature = r'C:\Users\ralnefai\Desktop\GIS610\Question 13\Question13.gdb\TractsWithinMaricopa'
xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis(tagetFeatcherClass, clip_features, out_feature, xy_tolerance)

print ('Tracts within Maricopa been clipped and New feature class created named TractsWithinMaricopa')
#-----------------------------------------------
