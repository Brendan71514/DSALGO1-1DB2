
userinput = float(input("type money\n"))
wiiaf=int(userinput/100)
wiineed=100-(userinput%100)

print("you can afford ", wiiaf," Nintendo Wiis. You will still need",
      wiineed,"amount of money to afford another additional wii")


f = int(input("enter number\n"))
ans=1
for i in range(1, f+1):
    ans = ans * i
print ("The factorial of ",f," is ",ans)

factorList = []
f=int(input("input num: "))

for x in range(1,f+1):
    if f%x==0:
        factorList.append(x)
        print("the factors of",f,"are ", factorList)



