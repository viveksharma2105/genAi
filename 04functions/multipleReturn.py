#example
def sum():
    pass
print(sum())  #None is returned because there is no return statement

#example 2
def number():
    return 10

no = number()
print(no)

#example 3 (early return)
def checkStatus(age):
    if age == 0:
        return "invalid age"
    return "valid age"
status = checkStatus(2)
print(status)

#example 4 (multiple return values)
def calculate(a, b):
    sum = a + b
    diff = a - b
    prod = a * b
    return sum, diff, prod
results = calculate(10, 5)
print("Results are:", results)

#another example of multiple return values
def report():
    return  "john", 25

name, age = report()
print('name: ', name)
print('age: ', age)