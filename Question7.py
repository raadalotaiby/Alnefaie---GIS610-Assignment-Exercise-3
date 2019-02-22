# Import system modules
import arcpy
arcpy.env.overwriteOutput = True


 
# Set local variables
inFeatures = r"C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb\CallsforService"
outLocation = r"C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb"
outFeatureClass = "FamilyFightCall"
delimitedField = arcpy.AddFieldDelimiters(inFeatures, "CFSType")
expression = delimitedField + " = 'Family Fight Call'"
 
# Execute FeatureClassToFeatureClass to create a new feature class based on call for service type 'Family Fight Call'
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, expression)

print ('Done')

