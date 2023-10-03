
class organism:

    def __init__(self,name,needed,provied,food=[]) -> None:
        
        self.name = name
        self.need = needed
        self.prov = provied
        self.food =food
