import json
from collections import namedtuple
 
class customerEntity:

    def __init__(self,full_name= None,cod=None):
        self.full_name = full_name
        self.cod = cod

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    
    def requestToClass(self,request):
        data = request.get_json() 
        data = json.dumps(data)
        values = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.full_name = values.full_name
        self.cod = values.cod