import math
def poistaparittomat(lista):
   return [n for n in lista if n%2==0]



lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)
print(poistaparittomat(lista))