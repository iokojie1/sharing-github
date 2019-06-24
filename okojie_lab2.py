#Irenosen Okojie
#June 24th, 2019
#GEOG682 Lab 2

import processing #import QGIS processing tools

crime_incidents = "S:/682/Summer19/iokojie/Crime_Incidents_in_2017/Crime_Incidents_in_2017.shp" #save shapefile as new variable 
iface.addVectorLayer(crime_incidents, "crime_incidents", "ogr") #add shapefile to map
polygon = "S:/682/Summer19/iokojie/Police_Districts/Police_Districts.shp" #save polygon to map
iface.addVectorLayer(polygon, "Police_Districts", "ogr") #add shapefile to map

#processing.runalg("qgis:mergevectorlayers", polygon, crime,"output_lab2.shp")

#processing.tools.general.runalg("qgis:mergevectorlayers", crime_incidents + ";" + polygon , "S:/682/Summer19/iokojie/output_lab2.shp")
#iface.addVectorLayer("S:/682/Summer19/iokojie/output_lab2.shp", "output_lab2", "ogr") 

#processing.runalg("qgis:joinattributesbylocation", polygon, crime_incidents, u'contains', 0, 1, 'sum', 1, "S:/682/Summer19/iokojie/output1_lab2.shp")
processing.runalg("qgis:joinattributesbylocation",{
                        "TARGET":polygon, 
                        "JOIN":crime_incidents,
                        "PREDICATE":u'contains',
                        "SUMMARY":0,
                        "KEEP":1,
                        "OUTPUT":"S:/682/Summer19/iokojie/output3_lab2.shp"})
                        
iface.addVectorLayer("S:/682/Summer19/iokojie/output3_lab2.shp", "output3_lab2", "ogr") 

#Distrct 3 had the most crimes
#5895 total crimes 