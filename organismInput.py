import OrganismClass

o = OrganismClass.organism

#names 
plantA = "plantA"
plantB = "plantB"
plantC = "plantC"

AnimalA= "AnimalA"
AnimalB= "AnimalB"
AnimalC= "AnimalC"
AnimalD= "AnimalD"
AnimalE= "AnimalE"
AnimalF= "AnimalF"
AnimalG= "AnimalG"


plant_list=[
    o(plantA,0,200),
    o(plantB,0,200),
    o(plantC,0,200),
]

org_list=[
    o(AnimalA,70,300,[plantB,AnimalC]),
    o(AnimalB,70,100,[AnimalA,plantC]),
    o(AnimalC,70,100,[AnimalB,AnimalD]),
    o(AnimalD,70,100,[plantA,AnimalC]),
    o(AnimalE,70,100,[AnimalB,AnimalC,AnimalA,AnimalD]),
    o(AnimalF,70,100,[AnimalB,AnimalE,AnimalA]),
    o(AnimalG,70,100,[AnimalB,AnimalA,AnimalD])
]

number_of_animals_to_be_selected =5