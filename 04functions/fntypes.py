#pure, impure, recursive, lambda(anonymous) functions
#pure function
def pure(a):
    return a*2
print(pure(5))  #10

#impure function(generally not recommended)
a = 10
def impure():
    global a
    a += 5
impure()
print(a)  #15

#recursive function
def factorial(n):
    if n == 0:
       return  1
    return n* factorial(n-1)
print(factorial(5))  

#lamdas functions
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango','apple']
filtered  = list(filter(lambda x:x  == 'apple',  fruits))
filtered1  = list(filter(lambda x:x  != 'apple',  fruits))
print(filtered)  
print(filtered1)
