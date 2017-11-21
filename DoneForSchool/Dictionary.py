list = []
list1 = []
D = open("Dictionary", "r")
Months = {}
for line in D:
    line = line.strip('\n')
    Month, Abbreviations = line.split(':')
    Months[Month] = Abbreviations







#statename = input("Enter the name of the state: ")
        #states[userinput] = statename
        #print(states)



Userinput = input(":")

Monthname = Months.get(Userinput)



print(Userinput, "Stands For", Monthname)

D = open("Dictionary", "w")
for m in Months:
    D.write(m+':'+str(Months[m])+'\n')

D.close()