# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name = name1 + name2
new_name2 = new_name.lower()
#true
t  = new_name2.count("t")
r  = new_name2.count("r")
u  = new_name2.count("u")
e  = new_name2.count("e")
true = t+r+u+e
#love
l = new_name2.count("l")
o  = new_name2.count("o")
v  = new_name2.count("v")
e  = new_name2.count("e")
love = l+o+v+e
final = int(str(true) + str(love))

if (final <10) or (final >90) :
    print(f"your score is {final}, you go togather like coke and mentos")
elif (final>=40) and (final >=50):
    print(f"your scoreis {final} , you are allright togather")
else:
    print(f"your score is {final}")

    





