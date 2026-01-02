#Tuples
spices = ("cardamom", "cinnamon", "cloves")
(first, second, third) = spices
print(f"First spice: {first}")


waterRatio, milkRatio = 1,5
print(f"Water to milk ratio: {waterRatio}:{milkRatio}")
waterRatio, milkRatio = milkRatio, waterRatio
print(f"After swapping : {waterRatio}:{milkRatio}") #swapped

#Memberships testing
cars = ["Toyota", "Honda", "Ford"]
print(f"Is Honda in the list ?: {'Honda' in cars}")

#Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(f"Fruits list: {fruits}")
fruits.remove("banana")
print(f"Fruits list after removal: {fruits}")

basketOne = ["apple", "banana"]
basketTwo = ["cherry", "date"]
print(f"Combined basket: {basketOne + basketTwo}")

basketOne.extend(basketTwo) #another way to combine lists
print(f"Extended basketOne: {basketOne}")

#Reversing lists
basketOne.reverse()
print(f"Reversed basketOne: {basketOne}")

#Sorting lists
basketOne.sort()
print(f"Sorted basketOne: {basketOne}")


#Built-in functions with lists
waterLevels = [1, 2,3,4,5]
print(f"Max water level: {max(waterLevels)}")
print(f"Min water level: {min(waterLevels)}")
print(f"Sum of water levels: {sum(waterLevels)}")
print(f"Length of water levels list: {len(waterLevels)}")


arr =  [ 9, 2, 6, 5] * 2
print(f"Array after multiplication: {arr}")
