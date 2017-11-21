list = []

score = int(input("how many numbers do you want to be added up"))

print("Enter The Numbers You Want Added Up")

for x in range(0,score):
    score1 = int(input())
    list.append(score1)

print("This Is Your Numbers", list)

AN = list # This Puts The List Into A Variable

S = sum(AN) # This Sums The Variable List To A Number Simple

print(S) # this Prints The Sum Of The Variable List