Dict = {"masala":"spicy",
        "Ginger":"Zesty",
        "Green":"Mild"}
print(Dict)
print(Dict.get("masala"))
for key,value in Dict.items():
    print(key,value)
    print(key ,Dict[key])
Dict["early Gray"]="Citrus"
print(Dict)
Dict.pop("Ginger")
print(Dict)
print(Dict.popitem())


# nested dictionary
college ={
    "branch":"cse",
    "ClassRoom":"Kc-204",
    "Section": 14,
    "Student" :{
    "Name":"Ashutosh",
    "height":5.11
    }
}
print(college)