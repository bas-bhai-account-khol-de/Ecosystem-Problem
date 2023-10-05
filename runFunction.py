import organismInput
from itertools import combinations
import copy
import utility

organisms = {}

for i in organismInput.org_list:
    organisms[i.name] = i

for i in organismInput.plant_list:
    organisms[i.name] = i



combinations_list = list(combinations(organismInput.org_list, organismInput.number_of_animals_to_be_selected))

# print((combinations_list))
working_combo = []

def findEco():
    for index,com in enumerate(combinations_list):
        print(index)
        satisfied = True
        com  = list(com) + organismInput.plant_list
        eco = {}
        for i in com:
            eco[i.name] = i
        eco_system = copy.deepcopy(eco)
        # print(eco)
        # print(eco_system)
        
        for org in com:
            if(org.need!=0):
                print(org.name)
                max_org =  utility.findmaxchild(org.food,eco_system)
                print("max organism",max_org)
                if(max_org == ""):
                    satisfied =False
                    break
                consumed = eco_system[max_org].prov - eco_system[org.name].need
                if( consumed <= 0 ):
                    satisfied = False
                    print("this combination wont work")
                    break;
                eco_system[max_org].prov = consumed 
                eco_system[org.name].need = 0
                # print("==========")
        if(not satisfied): 
            continue
        for org in com:
            if(eco_system[org.name].prov > 0  and satisfied):
                satisfied =True
            else:
                satisfied =False 
                continue
        if(satisfied):
            print("found Combination -----------------====================")
            temp = [str(index)]
            for org in com:
                print(org.name)
                temp.append(org.name)
            working_combo.append(temp)
            
            print("retuned Combination -----------------====================")
            # break # remove this if want multiple answers
        
findEco()

with open("output.txt", "w") as txt_file:
    for line in working_combo:
        txt_file.write(",".join(line) + "\n")

            



#### main algorithm
