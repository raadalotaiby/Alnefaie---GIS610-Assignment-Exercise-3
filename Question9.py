# Import system modules
import arcpy
from arcpy import env
env.overwriteOutput = True




#Create Feature Class
#-------------------------------------------
# Set local variables
out_path = r"C:\Users\ralnefai\Desktop\GIS610\Question5.gdb"
out_name = "parks"
geometry_type = "POLYGON"

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type)

print ('Done')

arcpy.env.workspace = r"C:\Users\ralnefai\Desktop\GIS610\Question5.gdb"

#Execute AddField to add new field
arcpy.AddField_management("parks", "Type", "TEXT", 9, "", "", "Type", "NULLABLE", "REQUIRED")
print ('New field Created')


# Set local parameters
domName = "ParksType"
gdb = out_path
inFeatures = "parks"
inField = "Type"
 
# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb, domName, "ParksType", 
                              "TEXT", "CODED")
    
# Store all the domain values in a dictionary with the domain code as the "key" 
# and the domain description as the "value" (domDict[code])
domDict = {"1":"local park", "2": "neighborhood parks", "3": "City park", 
           "4": "State park", "5": "National park"}

# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
    
# Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(inFeatures, inField, domName)


print ('Domain Created')