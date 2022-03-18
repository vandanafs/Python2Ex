import math
def exponentiate (x, y) :
  return math.pow(x,y)


def rise_to_fourth_power(a):
  return exponentiate(a,4)



print(exponentiate(2,4))
print(rise_to_fourth_power(3))

square=3
print(exponentiate(square,square))

square=lambda x:exponentiate(x,2);
print(square(4))

cube= lambda  y: exponentiate(y,3)
print("Cube of  value  ",cube(2))