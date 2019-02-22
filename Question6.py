# Import system modules
import arcpy

from arcpy import env
env.overwriteOutput = True

#add a field called ‘Crime_Explanation’
#-------------------------------------------
# Set environment settings
arcpy.env.workspace = r"C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb"
 
#Execute AddField to adad new fields
arcpy.AddField_management("CallsforService", "Crime_Explanation", "TEXT", 9, "", "", "Crime_Explanation", "NULLABLE", "REQUIRED")
print ('New field Created')
#-------------------------------------------

# if the value of field ‘CFSType’ is Burglary Call, write ‘This is a burglary’ into the field that you just added.
#-------------------------------------------
arcpy.env.workspace = r"C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb"
fc = r"C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb\CallsforService"
fields = ['CFSType', 'Crime_Explanation']

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    # Update the fields
    for row in cursor:
        if (row[0] == 'Burglary Call'):
            row[1] = 'This is a burglary'
        cursor.updateRow(row) 


print ('All Changes been made')
#-------------------------------------------