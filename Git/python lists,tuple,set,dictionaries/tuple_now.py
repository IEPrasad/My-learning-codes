## python tuples how to use methods

##1) count() bawithaya

#my_tuple = ("tuple","methods","have","tuple","tuple")
#print(my_tuple.count("tuple"))
##>>> 3

## mehidi apa laba dena kisiyam element ekak kopamana warayak yedi athidaii bala gatha hakiwe.
##___-------___----_---__--_--_--_--_-----__-__--_-

##2) index() bawithaya 
#my_tuple = (1,2,"apple",3,4,6)
#index = my_tuple.index("apple")
#print(index)
##>>> 2
## mehidi kisiyam element ekakata adala index number eka laba ganimata hakiwe
##------------________----------________---------_________--------__---_---__---

##3) len() bawithaya 

#my_tuple = ("apple","samsung","sony","chamara")
#x= my_tuple.len()
#print(x)
#>>> AttributeError: 'tuple' object has no attribue len 
## so how to use len() method

#my_tuple = ("apple","samsung","sony","chamara")
#x= len(my_tuple)
#print(x)
##>>> 4
## mehidi tuple ekehi length eka labe

##____----_________-----__________-----____-------__--__--_

##4) max() bawihaya 
#my_tuple = (1,2,3,4,676,8)
##print(max(my_tuple))
##>>> 676
## mema method ekada samanya yen yedi athi akrayata use kala nohaki wana athara 
## mehi yoda athi paraidi we.
## memagin maximum element eka labe


on tuples:

    count()

 python

my_tuple = (1, 2, 3, 4, 4, 4, 5)

# Count the number of times the value 4 appears in the tuple
count = my_tuple.count(4)

print(count)  # Output: 3

    index()

python

my_tuple = ('apple', 'banana', 'cherry', 'banana')

# Find the index of the first occurrence of 'banana'
index = my_tuple.index('banana')

print(index)  # Output: 1

    len()

python

my_tuple = ('apple', 'banana', 'cherry')

# Get the length of the tuple
length = len(my_tuple)

print(length)  # Output: 3

    max()

python

my_tuple = (10, 20, 30, 40)

# Get the maximum value in the tuple
maximum = max(my_tuple)

print(maximum)  # Output: 40

    min()

python

my_tuple = (10, 20, 30, 40)

# Get the minimum value in the tuple
minimum = min(my_tuple)

print(minimum)  # Output: 10

    sorted()

python

my_tuple = (5, 3, 8, 1, 7)

# Sort the tuple in ascending order
sorted_tuple = sorted(my_tuple)

print(sorted_tuple)  # Output: [1, 3, 5, 7, 8]

    sum()

python

my_tuple = (1, 2, 3, 4)

# Get the sum of all the values in the tuple
total = sum(my_tuple)

print(total)  # Output: 10

    any()

python

my_tuple = (False, False, True, False)

# Check if any value in the tuple is True
result = any(my_tuple)

print(result)  # Output: True

    all()

python

my_tuple = (True, True, False, True)

# Check if all values in the tuple are True
result = all(my_tuple)

print(result)  # Output: False

    tuple()

python

my_list = [1, 2, 3, 4]

# Convert a list to a tuple
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (1, 2, 3, 4)

































