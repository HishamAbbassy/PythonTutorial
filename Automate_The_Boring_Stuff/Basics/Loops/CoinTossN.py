import random

print(' Let us play Head or Tail')
print('How many times you want to play? ')

N = input('>')
N = int(N)
if N > 0:

    print('(H)ead or (T)ail?')
    S = input('>')
else:
    print('Good Bye')

def Head_Tail(n):

    h = 0
    t = 0

    for i in range(n):  # Perform 100 coin flips.

        if random.randint(0, 1) == 0:
            print('H', end=' ')
            h = h + 1

        else:
            print('T', end=' ')
            t = t + 1

    print('Head: ' + str(h) + ' ,Tail: ' + str(t))  # Print one newline at the end.
    return h, t

#Head_Tail (10)
#Head_Tail (100)
#Head_Tail(10000)

if S == 'H':
    h,t = Head_Tail (N)
   
    if h > t:
        print('You WON!')
    elif h == t:
        print('Draw')
    else:
        print('you Lost')

elif S == 'T':
    h,t = Head_Tail (N)
   
    if t > h:
        print('You WON!')
    elif h == t:
        print('Draw')
    else:
        print('you Lost')

else:
    print('Wrong Choice')