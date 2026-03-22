# stone paper scisssor
import random
robot= random.choice([1,0,-1])
yourstr= input("enter your input: ").upper()
youDict= {"R":1, "P":-1,"S":0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}  # ✅ Fix added

you= youDict[yourstr]
if(you == robot):
    print("draw")

# else:
#     if(robot == -1 and you==1 or robot == 1 and you==0 or robot == 0 and you==-1):
#     print("you loose")
# elif(robot ==1 and you==-1 or robot == 0 and you==1 or robot == -1 and you==0):
#     print("you win")
# else:
#     print("somthing went wrong")

# another optimize way to solve it

else:
    if((robot - you) ==-1 or (robot - you) ==2):
        print("you loose")
    else:
        print("you win")
print(f"computer choose {reverseDict[robot]}")