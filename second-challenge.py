

def secondchallenge(array):
    newpair = list(zip(array[::2], array[1::2])) ###pega do primeiro até o útlimo num salto de 2 e no ouro do indice 1 ao ultimo num salto de 2
    count = 0
    for i in newpair:
        count += 1 if (i[1]-1 == i[0] or i[1]+1 == i[0]) else 0
    return count

## versão top
def secondchallengev2(array):
    return sum([1 if (i[1]-1 == i[0] or i[1]+1 == i[0]) else 0 for i in list(zip(array[::2], array[1::2]))])

print(secondchallengev2([2,1,3,4,5,6,7,6]))