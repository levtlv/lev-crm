import csv
import simplekml

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyA-0wsvfO21mXFaARhw9Mj__3Ppca0h9wk')

# Geocoding an address

# Look up an address with reverse geocoding
inputfile = csv.reader(open('ganim.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
    gc = gmaps.geocode(row[3]+ ' תל אביב')
    gc = gc[0]
    try:
        kml.newpoint(name=row[0], coords=[(
            gc['geometry']['location']['lng'],
            gc['geometry']['location']['lat'])])
    except Exception as e:
        print("{} - {}".format(row[0], e))
        # import pdb; pdb.set_trace()
    print("{} - decoded".format(row[0]))

kml.save('battleplaces.kml')
