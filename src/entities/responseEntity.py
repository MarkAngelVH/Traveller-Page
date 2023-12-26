import json

class responseEntity:
    def __init__(self,status,message,entity):
        self.status = status
        self.message = message
        self.entity = entity
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)