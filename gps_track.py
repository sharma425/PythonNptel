from gmplot import gmplot
import csv

gmap = gmplot.GoogleMapPlotter(28.689169, 77.324448, 17)
gmap.coloricon = "http://www.googlemapsmarkers.vom/v1/%s/"

with open("countries.csv") as f:
    reader = csv.reader(f)
    k=0
    flag=True
    for row in reader:
        if flag ==True:
            flag=False
            continue
        lat = float(row[1])
        long = float(row[2])
        
        if (k==0):
            gmap.marker(lat, long, 'yellow')
            k=1
        else:
            gmap.marker(lat,long,'blue')
            
gmap.marker(lat, long, 'red')

gmap.draw("mymap.html")