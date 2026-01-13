import random

print(' Let us play Head or Tail')

def Head_Tail(n):

    h = 0
    t = 0

    for i in range(n):  # Perform n coin flips.

        if random.randint(0, 1) == 0:
            print('H', end=' ')
            h = h + 1

        else:
            print('T', end=' ')
            t = t + 1

    print('Head: ' + str(h) + ' ,Tail: ' + str(t))  # Print one newline at the end.
 

Head_Tail (10)
Head_Tail (100)
Head_Tail(10000)

