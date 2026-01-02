#immutable data types  in python
# not the  variable  changed, only the reference of the variable  is changed
suger = 2
print(f"1st  suger: {suger}")
suger = 12
print(f"2nd  suger: {suger}")

#to find the id of the  variable
print(f"ID  1st: {id(2)}")
print(f"ID  2nd: {id(suger)}")


#mutable data types in python
spice_mix =  set()
print(f"initial spice mix id: {id(spice_mix)}")

spice_mix.add("cinnamon")
spice_mix.add("ginger")
print(f"spice mix after additions: {id(spice_mix)}")