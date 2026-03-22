tea_varities=["black","Green","Oolong","white"]
print(tea_varities)
# sliceing of a list
print(tea_varities[1:4])
print(tea_varities[:2])
print(tea_varities[1:])
# it print the vales one by one as a indivisuL
# tea_varities[1:2]="lemon"
print(tea_varities)
tea_varities[1:2]=["lemon"]
print(tea_varities)
# for inserting the vaalues in the list
tea_varities[1:1]= ["test","test"]
print(tea_varities)
if "lemon" in tea_varities:
    print("i want lemon tea") 
tea_varities.insert(1,"green")
print(tea_varities)
tea_varities_copy= tea_varities.copy()
# we use .copy() function for changing the refrence in memory other wise if we do 
# tea_varities_copy = tea_varities 
# so if we change copy so it reflect on main memory

# making a list by using loop
square=[x**2 for x in range(1,9)]
print(square)