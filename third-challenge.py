matriz = [['m', 'y', 'e'], 
          ['x', 'a', 'm'], 
          ['p', 'l', 'e']]

def thirdchallenge(matrix, indexes):
    letters = [j for i in matrix for j in i]
    resp = ''
    for k in indexes:
        resp += ''.join(letters[k-1])
    return resp

## versao top
def thirdchallengev2(matrix, indexes):
    return ''.join([j for i in matrix for j in i][k-1] for k in indexes)

print(thirdchallenge(matriz, [3,6,9,1,2]))