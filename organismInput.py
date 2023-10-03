import OrganismClass

o = OrganismClass.organism

#names 
Coral = "Coral"
hornwort = "hornwort"
Java = "Java"

BlueTang= "BlueTang"
BullShark= "BullShark"
GiantTigerPrawn= "GiantTigerPrawn"
GultStur= "GultStur"
Guppy= "Guppy"
JapneseSpider= "JapneseSpider"
JellyFish= "JellyFish"
NorthenPike= "NorthenPike"
Orca= "Orca"
RainbowTrout= "RainbowTrout"


plant_list=[
    o(Coral,0,6140),
    o(hornwort,0,4930),
    o(Java,0,5730),
]

org_list=[
    o(BlueTang,1770,3770,[JapneseSpider,GiantTigerPrawn,BullShark,NorthenPike,Guppy,GultStur,Orca]),
    o(BullShark,1870,1100,[hornwort,Java]),
    o(GiantTigerPrawn,1220,1520,[hornwort,Java,Coral]),
    o(GultStur,1140,2960,[Orca,BullShark,hornwort,Coral,NorthenPike,Java]),
    o(Guppy,1570,3230,[Orca,BullShark,hornwort,Coral,NorthenPike,Java]),
    o(JapneseSpider,2200,4600,[hornwort]),
    o(NorthenPike,1810,2700,[hornwort,Java]),
    o(Orca,1700,3280,[hornwort,Java]),
    o(RainbowTrout,4030,4650,[Guppy,JapneseSpider,GultStur,Orca,GiantTigerPrawn,NorthenPike]),
    o(JellyFish,3430,3970,[hornwort])
]

number_of_animals_to_be_selected =5