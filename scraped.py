import xmltodict


data = xmltodict.parse(open(r'data\scraped\204.xml').read())['route']
#print(data.keys())

'''
print(data['route_title'])
print(data['route_description'])
print(data['cover_note'])
print(data['accessibility'])
print(data['airport'])
print(data['express'])
print(data['ferry'])
print(data['link'])
print(data['streetcar'])
print(data['nightowl'])
print(data['sounder'])
print(data['watertaxi'])
print(data.keys()) #@xmlns:xsi xs:schema route_title route_desciprtion cover_note accessibility airport express ferry link streetcar nightowl sounder watertaxi schedules

print(len(data['schedules']['schedule']))
for schedule in data['schedules']['schedule']:
    print (schedule['timetable']['trips']['trip'][0]['departures']['departure'])
    print('\n')

'''


class Route:
    def __init__(self,routeno):
        self.routefilename = 'data\scraped\{}.xml'.format(routeno)
        self.rawxml = open(self.routefilename,'r').read()
        self.parsed = xmltodict.parse(self.rawxml)['route']

        #actual parsed
        self.schedules = [schedule['when']+' '+schedule['direction'] for schedule in self.parsed['schedules']['schedule']]
        self.stops = {}
        for schedule in self.schedules:
            self.stops[schedule] = [schedule['departures']['departure'] for schedule in self.parsed['schedules']['schedule'][self.schedules.index(schedule)]['timetable']['trips']['trip']]
        #self.stops = [schedule['departures']['departure'] for schedule in self.parsed['schedules']['schedule'][0]['timetable']['trips']['trip']] #schedule['timetable']['trips']['trip'][0]['departures']['departure']


t = Route('204')
print(t.stops['Weekday To North Mercer Island'][0])