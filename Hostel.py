class Resident:
    def __init__(self, name, room_no):
        self.name = name
        self.room_no = room_no

class visitor:
        def __init__(self ,name ,R_name ,room_no):
             self.name = name
             self.Resident_name = R_name
             self.room_non = room_no
class Hostel:
     def __init__(self ,H_name ,address):
          self. name =H_name
          self.address = address
          self.visits = []

    def record_visit(self, visitor: visitor, resident: Resident)          
        
