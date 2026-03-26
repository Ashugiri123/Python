f = open("trash.txt")

data = f.read()
print(data)

f.seek(0)   # move pointer back to start

data = f.readlines()
print(data)

f.close()


#open a file and replace a word from the file
with open("trash.txt","r") as f:
    data= f.read()

new_data = data.replace("java","python")
print(new_data)

with open("trash.txt","w") as f:
    f.write(new_data)

#find a word in a file 
word = input()
with open("trash.txt","r") as f:
    data= f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Found")