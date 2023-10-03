

def findmaxchild(food,eco_system):
    max_org = ""
    max_cal = -1
    for f in food:
        
        if( (f in eco_system) and eco_system[f].prov  > max_cal):
            max_cal = eco_system[f].prov
            max_org = f
    return max_org