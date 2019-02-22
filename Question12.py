import arcpy
import os
import csv

#sitting up the Local variables:
featureClass = r"C:\Users\ralnefai\Desktop\GIS610\Exercise 3.gdb\Exercise 3.gdb\General_Offense"
fieldNames = ['locationTranslation', 'OffenseCustom']
cursorFields = ";".join(fieldNames )

#sitting up the filter statment:

filterStatement = "OffenseCustom='BURGLARY FORCE' and locationTranslation='Residence/Home'"
crimeCount = 0

#write the results to a CSV file:
with open('burglariesInResidenceHome.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(fieldNames)
	with arcpy.da.SearchCursor(featureClass, fieldNames, filterStatement) as cursor:
		for row in cursor:
			crimeCount += 1
			filewriter.writerow(row)


print ("Total burglaries in Residence Home are " + str(crimeCount))