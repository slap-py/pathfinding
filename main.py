import csv
import json

data = {}

def openFile(path,primary):
    with open(path,'r') as csvf:

        csvreader = csv.DictReader(csvf)
        for rows in csvreader:
            key = rows[primary]
            data[key]=rows
    print('returning',path)
    return data

trips = openFile(r'data\KCMetro\trips.txt','trip_id')
stops = openFile(r'data\KCMetro\stop_times.txt','stop_id')

tripStops = {}
for stopi in list(stops.keys()):
    stop = stops[stopi]
    if stop['trip_id'] in list(tripStops.keys()):
        tripStops[stop['trip_id']].append(stop)
    else:
        tripStops[stop['trip_id']]=[stop]
       

f = open('output.json','w')
f.write(json.dumps(tripStops))
f.close()


