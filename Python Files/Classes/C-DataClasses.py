from dataclasses import dataclass,field
import random,string

def generate_id() :
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass
class Person():
    name:str
    address:str
    active:bool=True
    Emails:list[str]=field(default_factory=list)         #default_factory=list means the default value is list
    id:str=field(init=True,default_factory=generate_id)  #init =True mean you can have it as a parameter 
    
def main ():
    man =Person("Robert","25 allyWay NewYork",id="2")
    print(man)    
main()    