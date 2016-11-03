##incident class for incident map
##stakeholder demo1 edition

import location_class.py
import date


class Incident:
    def __init__(self, _event_num, _event_type, _location, _description):
        self.event_num = _event_num
        self.event_type = _event_type
        self.location = _location
        self.event_description = _description
        
        
