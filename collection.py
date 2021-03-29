#collections: counter
from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque

a= "aaaabbbbssgsiskdjkhnaaa"
my_count=Counter(a)
print(my_count.most_common(1)) #gives the first most common
print(my_count.most_common(1)[0]) # gives the tuple as the most common returns a list of tuple
print(my_count.most_common(1)[0][0]) # returns just the element
print(list(my_count.elements())) # gives a list of all elements inside a touple

#collectiond: namedtouple , lightweight object type
point= namedtuple('point','x,y') # creates a class with name as point and x,y are how we want the points to be represented as
pt= point(1, 2)
print(pt)

#collections: ordered dictionary
#after python 3.7 all insertion to dict are ordered else we use this

#collection: default dict, same as dictionary with diff of having a default key
d=defaultdict(int)
d['a']=1
d['c']=7
print(d['e']) # if key not available it prints the value 0 depending on the data type

#collections : deque double ended queue; functions performed from both sides 
d= deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(7) # appends to the left 
d.appendleft(8)
d.pop() #pops the value on the right most
d.popleft() #pops leftmost value
d.extend([1,2,4,68]) #adds a list to the right 
d.extendleft([3,5,6]) #starts adding values to the left from first 
print(d)

