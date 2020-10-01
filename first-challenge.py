def firstchallenge(array):
    sum = 0
    for num in array: 
        sum += num if array.count(num) == 1 else 0 
    return sum

## versão top
def firstchallengev2(array):
    return sum([num if array.count(num) == 1 else 0 for num in array])

print(firstchallengev2([4,5,7,5,4,8]))