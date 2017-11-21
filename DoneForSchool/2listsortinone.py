n=int(input("How many numbers do you want to enter: "))

list = [] #An empty list to enter data into

print("Enter",n ,"numbers: ")
for index in range(0,n): #A loop that runs n times
    UserInput = int(input()) #user input read as an int into the Var UserInput
    list.append(UserInput) #Add the user input to the list

print("You have entered:") #This prints the list back to the user so they can check it
for index in list:
    print(index)
t=int(input("How many numbers do you want to enter: "))

list1 = [] #An empty list to enter data into

print("Enter",t ,"numbers: ")
for index1 in range(0,n): #A loop that runs n times
    UserInput1 = int(input()) #user input read as an int into the Var UserInput
    list1.append(UserInput1) #Add the user input to the list

print("You have entered:") #This prints the list back to the user so they can check it
for index1 in list1:
    print(index1)

#SORTING GOES HERE!
jlist = []

for x in list:
    jlist.append(x)

for x in list1:
    jlist.append(x)

slist = []
for x in jlist:
    inserted = False
    if (len(slist) == 0):
        slist.append(x)
        inserted = True

    index = 0
    while(index < len(slist) and not inserted):
        if(slist[index] >= x):
            slist.insert(index, x)
            inserted = True
        index += 1

    if(not inserted):
        slist.append(x)


####

print("Sorted list:") #Print the sorted list
for i in slist:
    print(i)