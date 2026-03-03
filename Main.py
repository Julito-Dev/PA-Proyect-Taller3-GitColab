class vehiculo:
    def __init__(self,matricula):
        self.matricula=matricula
        
    
    #All vehicles can ride around the world.     
    def Ride():
        raise NotImplementedError


class Car (vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)


    #@Override 
    def ride():
        print("Your Car is now riding on the road. Great!")
    
    
class motorbike (vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
    
    #@Override
    def Ride():
        print("Your motorbike is now riding on the road. Amazing!")
