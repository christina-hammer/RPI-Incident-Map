##Incident cache
##THIS CODE IS CRACKED-OUT NONSENSE I WROTE ON A PLANE WITH NO WIFI
## DO NOT USE UNTIL REVIEWED FURTHER 11/2 


import location_class.py
import incident_class.py

##this thing should probably import/know about the database

class IncidentCache:
     def __init__(self, _begin_date, _end_date):
          self.incident_by_event = {} #dictionary of incidents sorted by event type
          self.locations = {} #dic of (location object, # incidents in location) pairs
          
          ##use python date time module for this
          self.begin_date = _begin_date #date object from python built-in module
          self.end_date = _end_date #date object from python built-in module
          
          self.setCacheByDateRange(self.begin_date, self.end_date) #to execute initial cache population
          
          
     ##returns list of incidents corresponding with a specified type
     def getType(self, spec_type):
          return self.event_type_dic[spec_type]
          
     ##takes in an incident object and adds it to the event_type_dic and
     ##adds or increments an entry to the locations dictionary
     ##be warned, I have done zero error checking as of yet
     def insertIncident(self, incid_obj):
          print("")
          ##if the event type for this incident is already in the dictionary
          ##add an entry to the event_type's individual dictionary for the new incident
          ##that belongs in that event type
          if(self.event_type_dic[incid_obj.event_type]):
               self.event_type_dic[incid_obj.event_type][incid_obj.event_num] = incid_obj
               
          else: ##if no key in dic for incid_obj's event_type, make one and add incid_obj to the val dictionary for it
               self.event_type_dic[incid_obj.event_type] = {incid_obj.event_num, incid_obj}
               
          ##now update locations
          if (self.locations[incid_obj.location]): #if location already present, increment
               self.locations[incid_obj.location] += 1
          else:
               self.locations[incid_obj.location] = 1 #if location not present, add to dic
               
               
          
     #set_begin_date and set_end_date both should be python date objs
     #input currently assumed to be valid for momment. erroe checking into be added
     def setCacheByDateRange(self, set_begin_date, set_end_date):
          ##currently writing this without being able to actually check syntax for
          ##date built-in functionality. Taking educated guesses
          
          ##if new time period has overlap, just blank event_type dictionary values and 
          ##locations counts. but keep the keys since they will likely be re-asses
          if ((set_begin_date > self.end_date) or (set_end_date < self.begin_date)):
               for t in self.event_type_dic:
                    t = {} #not sure if need a .value
               for l in locations:
                    l = 0
          else: ##check to see if incidents should be deleted b/c out of new date range
               for t in self.event_type_dic:
                    for i in t:
                         #i.value should be the incident object
                         #can't remember how to access the value while looping through dic rn
                         #still no wifi
                         if ((i.value.date_occurred > set_end_date) or (i.date_occurred < set_begin_date)): #if date in dictionary is outside of new range, erase it
                              
                              self.locations[i.value.location] -= 1
                              self.event_type_dic[i.value.event_type].erase(i)
          
          #self.location counts and self.event_type_dic should now only refelect valid 
          #incidents for the new date range. 
          
          ##now new incidents from the DB that qualify for the new date range need 
          ##to be added to the cache
          
          ##
          ## db will be imported/accessible by the cache, 
          ## db will be given date parameters to use to return queries that are valid 
          ##for database entries in data range:
          ##    if (!self.event_type_dic[(querey result's incident #)] in dictionary)
          ##      Inciudent i = Incident(*query information!*)
          ##      self.insertIncident(i) ##this will update event_type_dic and locations
          ## 
          ##
          ##
          
          #now after removing out-of-range entries and adding new ones, 
          #see if any empty event types or locations left that need to e deleted
          
          for t in self.event_type_dic:
               if (t.empty): ##if no incidents affiliated with an event type
                    self.event_type_dic.erase(t) ##erase that event type 
          
          for l in self.locations:
               if(l.value == 0): 
                    self.locations.erase(l)
          
          #check beginning < end for all given vals
          #check end and begin valid for all available data
          #if end is before current beginning or beginning > current end
          ##erase everything, run totally new insertion query
          
          
          
          
          
