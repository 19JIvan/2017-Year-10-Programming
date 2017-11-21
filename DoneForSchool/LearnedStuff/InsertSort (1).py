n=int(input("How many numbers do you want to enter: "))

list = [] #An empty list to enter data into

print("Enter",n ,"numbers: ")
for index in range(0,n): #A loop that runs n times
    UserInput = int(input()) #user input read as an int into the Var UserInput
    list.append(UserInput) #Add the user input to the list

print("You have entered:") #This prints the list back to the user so they can check it
for index in list:
    print(index)

#SORTING GOES HERE!
slist = []

for x in list:
    inserted = False
    if(len(slist)==0):
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