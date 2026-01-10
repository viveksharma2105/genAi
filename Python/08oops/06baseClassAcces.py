class Chai:
    def __init__(self,type_, strength):
        self.type = type_
        self.strength = strength

# #inherit (but here is duplication)
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spiceLevel):
#         self.strength = strength
#         self.type =  type_
#         self.spiceLevel = spiceLevel

# #Another way to inherit without duplication but here is explicit call of  inherited class
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spiceLevel):
#         Chai.__init__(self,type_, strength)
#         self.spiceLevel = spiceLevel
        
        

#Optimal  way to inherit class {super() method}
class GingerChai(Chai):
    def __init__(self, type_, strength, spiceLevel):
        super().__init__(type_, strength)
        self.spiceLevel = spiceLevel
