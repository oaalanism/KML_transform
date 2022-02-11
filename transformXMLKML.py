from unicodedata import name
from urllib import request
from xml.dom import minidom

import os

import simplekml

link = "https://www.tanlib.com/getKML3.php?id="

colors = {
    2: simplekml.Color.rgb(247, 11, 11),
    3: simplekml.Color.rgb(51, 127, 51),
    4: simplekml.Color.rgb(41, 236, 223),
    5: simplekml.Color.rgb(255, 153, 153),
    6: simplekml.Color.rgb(0, 0, 153),
    7: simplekml.Color.rgb(102, 204, 0)
}

for i in range(2, 8):
    xmlPath = "./XML/Line-"+str(i-1)+".xml"
    url = request.urlretrieve(link+str(i), xmlPath)
    xmlDoc = minidom.parse(xmlPath)


    kml = simplekml.Kml(name="Niort Line "+str(i-1))
    
    linestrings = xmlDoc.getElementsByTagName('LineString')
    
    color = colors[i]
    for j in range(len(linestrings)):
        c = linestrings[j].getElementsByTagName("coordinates")[0].firstChild.data
        #labelStyle = xmlDoc.getElementsByTagName("LabelStyle")[0]
        #color = labelStyle.childNodes[1].firstChild.data
        values = c.split(" ")
        coords = []
        for v in values:
            coord = v.split(",")
            map_object = map(float, coord)
            m = list(map_object)
            coords.append(m)
        ls = kml.newlinestring(name = "line-"+str(j))
        ls.style.linestyle.color = color
        ls.coords = coords
        #ls.altitudemode = simplekml.AltitudeMode.relativetoground
    kmlPath = "./KML/Line-"+str(i-1)+".kml" 
    kml.save(kmlPath)
    #kml.save("Saving.kml")
        