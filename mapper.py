import organismInput
from itertools import combinations
import copy
import utility



def printEcosystem(ecos):
    es = {}
    for key in ecos:
        es[key] = {
            "provided":ecos[key].prov,
            "need":ecos[key].need

        }
    print(es)

index  = 133
combinations_list = list(combinations(organismInput.org_list, organismInput.number_of_animals_to_be_selected))
com = combinations_list[index]
com  = list(com) + organismInput.plant_list
eco = {}
for i in com:
    eco[i.name] = i
eco_system = copy.deepcopy(eco)

for org in com:
    if(org.need!=0):

        max_org =  utility.findmaxchild(org.food,eco_system)
        
        if(max_org == ""):
            satisfied =False
            break
        consumed = eco_system[max_org].prov - eco_system[org.name].need
        if( consumed <= 0 ):
            satisfied = False
            print(max_org , "remaning : " ,consumed ,"  " ,org.name," needed_more: ", 0)
            print("this combination wont work")
            break;
        eco_system[max_org].prov = consumed 
        eco_system[org.name].need = 0
        print("organism" , org.name,"ate",max_org)

        print(max_org , "remaning : " ,eco_system[max_org].prov ,"  " ,org.name," needed_more: ", eco_system[org.name].need )
        printEcosystem(eco_system)
        print("==========")
        input("press enter .....")