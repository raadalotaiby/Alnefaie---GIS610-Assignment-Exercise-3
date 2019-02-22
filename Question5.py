import arcpy
arcpy.env.overwriteOutput = True

#-----------------------------------------------
#Ceating New GDB
GDBLocation = r'C:\Users\ralnefai\Desktop\GIS610'
GDBName = 'Question5'

arcpy.CreateFileGDB_management (GDBLocation, GDBName)

print ('Your GDB been Created')
#-----------------------------------------------



#-----------------------------------------------
#Creating feature classes within the New GDP


#all the variables
currentworkspace = r'C:\Users\ralnefai\Desktop\GIS610\Question5.gdb'
geometryType = 'POLYGON'
spatialRef = arcpy.SpatialReference(3395)

#list of feature classes
featureClassNameList = ['CapitalCities','Landmarks','HistoricPlaces','StateNames','Nationalities','Rivers']

#sitting the arcpy default workspace
arcpy.env.workspace = currentworkspace


#this is a funcation to create a new polygon feature class
def creatFeatureClass(inFeatureClassName):
    arcpy.CreateFeatureclass_management(currentworkspace
                                        ,inFeatureClassName
                                        ,geometryType
                                        ,''
                                        ,'DISABLED'
                                        ,'DISABLED'
                                        ,spatialRef)
    print('Created feature class called ' + inFeatureClassName)
#End of function

#run the function or call the feature 

for newFeatures in featureClassNameList:
    creatFeatureClass(newFeatures)