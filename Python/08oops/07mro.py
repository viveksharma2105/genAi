#MRO = Method Resolution Order ## Multiple inheritance
class A:
    label = "A: Base Class"
    
class B(A):
    label = "B: inherit class A"
    
class C(A):
    label = "C: inherit class A"
    
class D(B,C):
    pass
    
cls = D()

#as D 1st inherit class B so the lable  printe is of B
print(D.label)

print(D.__mro__)

