import random

n=int(input("How many numbers do you want to generate: "))

list = [] #An empty list to enter data into

print("Enter",n ,"numbers: ")
for index in range(0,n): #A loop that runs n times
    UserInput = random.randrange(1, 100)
    list.append(UserInput) #Add the input to the list

print("You have generated:") #This prints the list back to the user so they can check it
for index in list:
    print(index)



Si = 0
Li = len(list)
while(Si < Li):
    i = Si

    n = list.pop(i)
    Li -= 1
    while(i<Li):
        if(list[i] > n):
            n2 = list[i]
            list[i] = n
            n = n2
        i += 1
    list.insert(i, n)
    if(not Si < Li):
        break
    i = Li
    n = list.pop(i)
    i -= 1
    while(i>Si-1):
        if(list[i] < n):
            n2 = list[i]
            list[i] = n
            n = n2
        i -= 1
    list.insert(Si, n)
    Si += 1




print("Sorted list:") #Print the sorted list
for i in list:
    print(i)
