import csv

f = open('final526.csv', 'r')

with f:

    reader = csv.DictReader(f)
    
    for row in reader:
        print("{ location: new google.maps.LatLng("+row['Lat']+","+ row['Long']+ "), weight: "+ str((float(row['ConfirmedCases'])/1000.0)) + "},")
