#set are immutable collection of data and it is unordered collection of data

collection ={1,2,3,4,4,5,0,"hello"}
print(collection)
print(len(collection))

col1 = {}#we can't use that for empty set it is used for denoting empty dictionary
col2 = set()#we use that for empty set
print(type(col1))
print(type(col2))

#in set we can't have duplicate values and it is unordered collection of data
# we can't access the element of set by using index because it is unordered collection

#functions of set
collection.add("world")# we can add the element in set by using add function
print(collection)
collection.remove(4)# we can remove the element by using remove function
print(collection)
collection.discard(5)# we can also remove the element by using discard function but if the
col2.add(5)
col2.add(6)
col2.add(7)
col2.clear()# we can clear the set by using clear function
print(col2)
print(collection.pop())# we can remove the random element by using pop function

col2.add(5)
col2.add(6)
col2.add(7)
print(collection.union(col2))# we can combine two sets by using union function
col2.add("hello")
print(collection.intersection(col2))# we can find the common element by using intersection function