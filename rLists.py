from random import randint
import time
cou = 10
li = []
while cou > 0:
    rNum = randint(1,10)
    li.append(rNum)
    cou = cou - 1
    time.sleep(0.1)
    print(li)