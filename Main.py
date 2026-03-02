class vehiculo:
    def __init__(self,matricula):
        self.matricula=matricula
        
    
    #All vehicles can ride around the world.     
    def Ride():
        raise NotImplementedError
