# Design a Parking Lot

## Clarifying Questions
 - Does the parking lot have multiple floors?
 - Are we dealing with just one parking lot or a chain of lots each having it's own address/name?
 - Are there going to be different types of spots for different types of vehicles? If we're only dealing with cars, what are the different types of cars? (Compact, SUV, Electric, etc)
 - The parking ticket will be given at the gate right?
 - Should the drivers pay while exiting?
 - What parking strategy will we implement?


 ## Design Reqs
 - A Car class for the different types of cars
 - A ParkingLot class that has details about the lot, like num floors.
 - A Floor class that holds details like num spots
 - A ParkingSpot class to track the availability of the spot and the vehicle parked in it
