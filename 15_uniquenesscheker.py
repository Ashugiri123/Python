# code for detecting dupicate item present in it or not
item =["banana","apple","orange","banana"]
unique_items = set(item)#because it will remove the duplicate
for item in item:
    if item in unique_items:
        print(item)
        break
    else:
        unique_items.add(item)