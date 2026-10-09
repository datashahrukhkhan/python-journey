


from calculator import addition

print(addition.add(10, 20))


# you can write:-
from calculator.addition import add

print(add(10, 20))




# Multiple modules import karna
from calculator.addition import add
from calculator.subtraction import subtract

print(add(20, 10))
print(subtract(20, 10))



# import package.module
import calculator.addition

print(calculator.addition.add(10, 5))








