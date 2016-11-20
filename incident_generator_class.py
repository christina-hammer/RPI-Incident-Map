
import json
#import incident_class
#import location
from datetime import date
from datetime import time


class Location:
    def __init__(self, _description):
        self.coords = '0, 0' #set value if possible. If not, use a default
        self.description = _description
          
    def setCoords(self, _coords):
        self.coords = _coords

##this will be initialized using strings and datetime objects created from the information in the mongo db entries 
class Incident:
    def __init__(self, _event_num, _incident_type, _location, _date_occurred, _date_reported):
        self.event_num = _event_num #int
        self.incident_type = _incident_type #string
        self.location = _location #location description
        #self.event_description = _description #string
        
        ##just use python built-in date objects for these::
        self.date_reported = _date_reported #datetime.date
        self.date_occurred = _date_occurred #datetime.date

class JsonToIncident:
    
    def __init__(self):
        self.begin_date = date(2016, 10, 1)
        self.end_date = date(2016, 10, 31)
        
    def createIncidents(self, json_fname):
        
        incidents = []
        
        with open(json_fname) as f:
            incid = json.load(f) #list of dictionaries containing json info
              
        
        print(len(incid)) #dictionary with key values ['disposition','date and time occurred from to occurred to','location','incident','date reported','event #', '_id']
        d = self.begin_date
        i = 0
    
        while (i < len(incid)):            
            inc = incid[i]
            inc_date_occ = inc['event #'].split("-")
            date_occurred = date(2000 + int(inc_date_occ[0]), int(inc_date_occ[1]), int(inc_date_occ[2]) )
                        
            if(date_occurred >= self.end_date):
                break
            elif (date_occurred >= self.begin_date):
                #print(inc)
                inc_date_rep = inc['date reported'].split(" ", 1)
                inc_date_rep = inc_date_rep[0].split("/")
                date_reported = date(2000 + int(inc_date_rep[2]), int(inc_date_rep[0]), int(inc_date_rep[1]))
                
                loc = Location(inc['location'])
                inc = Incident(inc['event #'], incid[i]['incident'], loc, date_occurred, date_reported)
                
                incidents.append(inc)
            i = i + 1
               
            
        return incidents
    
    def setDateRange(self, _begin, _end):
        assert(_begin <= _end)
        self.begin_date = _begin
        self.end_date = _end
        
class IncidentToJson():
    
    def __init__(self):
        pass
    
    def createJson(self, incidents):
        
        fname = 'incidents.txt'
        
        
        with open(fname, 'w') as json_file:
            for incid in incidents:
                j_inc = {'event #': incid.event_num, 'incident_type': incid.incident_type, 'location': incid.location, 'date reported': incid.date_reported.isoformat(), 'date_occurred': incid.date_occurred.isoformat()}
                json.dump(j_inc, json_file)
        
        json_file.close()
        
        return fname
        
#holds selection of incidents based on date range 
class IncidentCache:
    
    #init will take in date objects made outside of the cache class in the main function upon start up reflecting the range of dates in the database that we want to pull incidents from
    def __init__(self):
        self.incidents = [] #list of incident objects                                  
        
    def setCacheContents(self, l):
        self.incidents = l
                             
    

def main():    
    cache = IncidentCache()
    
    j_to_i = JsonToIncident()
    j_to_i.setDateRange(date(2016, 10, 1), date(2016, 10, 5))
    
    cache.setCacheContents(j_to_i.createIncidents("test.json"))
    i_to_j = IncidentToJson()
    i_to_j.createJson(cache.incidents)
    
if __name__ == "__main__":
    main()
        