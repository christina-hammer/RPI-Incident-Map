##Incident cache
##stakeholder1 demo edition
##adding incidents and filtering by type implemented


import location_class.py
import incident_class.py

class IncidentCache:
     def __init__(self):
          
          #{("event_type", [Incident_obj1, Incident_obj2, Incident_obj3...])}
          #dictionary<string, list<Incident>>
          self.incident_by_type = {}
          
          #{(location_obj, (# of occurences for all incident types))}
          self.locations = {}
          
          
     ##returns list of incidents corresponding with a specified type
     ##or empty list if type isn't in the dictionary
     def getType(self, spec_type):
          if (spec_type in self.incident_by_type):
               return self.incident_by_type[spec_type]
          else:
               return []
          
     ##takes in an incident object and adds it to the event_type_dic and
     ##adds or increments an entry to the locations dictionary
    
     def insertIncident(self, incid_obj):

          ##if the event type for this incident is already in the dictionary
          ##add an entry to the event_type's individual dictionary for the new incident
          ##that belongs in that event type
          if(incid_obj.event_type in self.incident_by_type):
               self.incident_by_type[incid_obj.event_type].append(incid_obj)
               
          else: ##if no key in dic for incid_obj's event_type, make one and add incid_obj to the val dictionary for it
               self.incident_by_type[incid_obj.event_type] = [incid_obj]
               
          ##now update locations
          if (self.locations[incid_obj.location]): #if location already present, increment
               self.locations[incid_obj.location] += 1
          else:
               self.locations[incid_obj.location] = 1 #if location not present, add to dic
               
               
       
