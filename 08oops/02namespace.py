class Chai:
    origin = "India"
    
    
print(Chai.origin)

Chai.ishot = True
print(Chai.ishot)

#creating objects from class chai

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.ishot}")


#change  value  by object
masala.ishot =  False
print(masala.ishot)
print(Chai.ishot)

#del from thhe object
del masala.ishot
print("After del the FalseHot: ",masala.ishot)

#adding new  to object
masala.flavour = "lemon"
print("flvour:",masala.flavour)


