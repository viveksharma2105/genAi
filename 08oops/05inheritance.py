class BaseChai:
    
    def __init__(self, type_):
        self.type =  type_
        
    def prepare(self):
        print(f"Preparing {self.type} chai...")
        
        
#we use parnthesis  with class for inherit the  class
class MasalaChai(BaseChai):
    
    def add_spices(self):
        print("Adding cardamom, cinnamon, and ginger...")
        
        
        
        
#aanother way 
class  ChaiShop:
    chaicls = BaseChai #not inherit but taking the refrence of BaseChai class
    def __init__(self):
        self.chai = self.chaicls("Regular")
        
    def serve(self):
        print(f"serving  {self.chai.type} chai in the shop")
        self.chai.prepare()
            
class FancyChai(ChaiShop):
    chaicls = MasalaChai #inherit the MasalaChai class
    
    
shop = ChaiShop()
fancy  = FancyChai()
shop.serve()
fancy.serve()
fancy.chai.add_spices()