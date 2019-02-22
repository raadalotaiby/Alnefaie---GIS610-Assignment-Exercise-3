# Import system modules
import arcpy

#calculate the number of features in a feature class
fc = r'C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb\CallsforService'
result = arcpy.GetCount_management(fc)
count = int(result.getOutput(0))
print(count)