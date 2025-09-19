import random
import math
pisteet=0
ympyrässä=0
while pisteet<1000000:
    x=random.uniform(-1.00,1.00)
    y=random.uniform(-1.00,1.00)
    pisteet+=1
    if x**2+y**2<1:
        ympyrässä+=1

pi=4*ympyrässä/1000000
print(pi)








