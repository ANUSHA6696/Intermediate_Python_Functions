#itertools: iterative tools used. 1.product
#product is given as a cartesian result
from itertools import product
a=[1,2,3]
b=[4,5,6]
prod=product(a,b, repeat=1) #repeat is given to repeat the number of times element is considered
print(list(prod)) #gives just an object so print with list

#itertools: permutation
from itertools import permutations
d=[1,2,3,4]
perm = permutations(d) #length  can also be mentioned but not mandatory
print(list(perm))

#itertools:combination 
from itertools import combinations,combinations_with_replacement
z=[1,2,3]
comb= combinations(z,2) #length is mandatory, this does not include self combination
comb_wr=combinations_with_replacement(z,3) #to include self value
print(list(comb))
print(list(comb_wr))

#accumulate
from itertools import accumulate
n=[1,2,4,5,3]
acc=accumulate(n, func=max) #func can be used to give various operations
print(list(acc)) #accumulated sum of prev result and next value

#groupby
from itertools import groupby

def even_numbers(x):
    if(x%2==0):
        return True
    else:
        return False

a=[1,3,4,6,4,5,4]
grp= groupby(a, key= even_numbers) #can be a func or a lambda func, groups a based on condition in the key
for key,value in grp:
    print(key,list(value))

#count,cycle and repeat are known to iterate infinite times