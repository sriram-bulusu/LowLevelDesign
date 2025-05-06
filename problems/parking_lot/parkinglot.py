class ParkingSpot:
    def __init__(self, spot_id: str, vehicle_type: int):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.is_spot_occupied = False

    def is_occupied(self) -> bool:
        return self.is_spot_occupied

    def park_vehicle(self):
        self.is_spot_occupied = True
    
    def unpark_vehicle(self):
        self.is_spot_occupied = False
    
    def get_spot_id(self) -> str:
        return self.spot_id

    def get_vehicle_type(self) -> int:
        return self.vehicle_type
    

class ParkingLevel:
    pass



# Parking Lot should be a singleton class
class ParkingLot:
    pass



class Vehicle:
    pass