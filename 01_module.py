import pyjokes

print("printing jokes....")
joke = pyjokes.get_joke()
print(joke)
#  imputable Data tyoe integer,float,bool,string,tuple,frozen set ,bytes
# mutable data  type list,set, dictionsry,bytearrrsy,arrray

# for ex:- 
x=10
y=x
x=15
print(x,y)
# y does not change because they point towards the address of value
# dictunary are called by key bbut tuple is use index for exicution
# if we have list inside the list so we use copy.deepcopy(h1) where h1 is that list rather than you can use only copy.copy(h1)  