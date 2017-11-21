#'Entry':'Definition'
states = {
    'VIC':'Victoria',
    'NSW':'New South Whales',
    'QLD':'Queensland',
    'TAS':'Tasmania',
    'NT':'Northern Territory',
    'WA':'Western Australia',
    'SA':'South Australia'
}

print("Enter the initials of a state to look up")
userinput = input(":")

statename = states.get(userinput)

#OPTIONAL CODE FOR ADDING MISSING ENTRIES
if(statename == None):
    print("This state does not exist, would you like to add it? (y/n)")
    a=input("")
    if(a=='y'):
        statename = input("Enter the name of the state: ")
        states[userinput] = statename
        print(states)
#END OPTIONAL CODE


print(userinput, "stands for", statename)

