import random
import time

X = ""
C = 0;
M = True;
E = False;
T = False;
play1 = False;
play = False;



print("Hello, Your Playing Double Or Nothing");




O = open("score", "r");
U = open("Name", "r");



hscore = [];
hName = [];



for line in O:
    hscore.append(int(line));
for line1 in U:
    hName.append(line1.strip('\n'));


print()
print()
print("1st Place", hName[0], "With A Score Of", hscore[0]);
print("2nd Place", hName[1], "With A Score Of", hscore[1]);
print("3rd Place", hName[2], "With A Score Of", hscore[2]);
print("4th Place", hName[3], "With A Score Of", hscore[3]);
print("5th Place", hName[4], "With A Score Of", hscore[4]);
print()
print()

O.close();

print("The Number You Start With Is 1, So Double Or Nothing: ");
print("Hint: Use Dub Or Stay To Play");
I = input();

O = open("score", "w");
U = open("Name", "w");

score = 2;


while M:

    if I == "Dub" or I == "dub":
        play = True;
        play1 = True;
        M = False;

    if I == "Stay" or I == "stay":
        play = True;
        play1 = True;

    if I != "dub" and I != "Dub":
        print("Please Enter Dub Or Stay");
        I = input();


while play1:

    if E:
        print("Double Or Nothing: ");
        I = input();

    if I == "Dub" or I == "dub":
        play = True;

    if I == "Stay" or I == "stay":
        play = True;
        T = True;

    if I != "stay" and I != "Stay" and I != "dub" and I != "Dub":
        print("Please Enter Dub Or Stay");

    while play:
        r = random.randrange(0, 101);
        time.sleep(3);

        if T:
            T = False;
            play = False;
            break;

        if r > 25:
            score *= 2;
            E = True;
            play = False;
            print("Your Score Is", score);

        else:
            print("You Lose");
            time.sleep(1);
            print("Play Again");
            Y = input();

            if Y == "yes" or Y == "Yes":
                break;

            else:
                play1 = False;
                play = False;
                break;



if score != 0:
    print("Your Score Was", score);
    X = input("Please Type Your Name In");



Y = open("Output", "w");
Y1 = open("Output1", "w");


Y.write(str(score));
Y1.write(X);



Y.close();
Y1.close();



Y1 = open("Output1", "r");
Y = open("Output", "r");


list = []; #An empty list to enter data into
list1 = [];
jlistn = [];
jlists = [];
sscore = [];
sName = [];



for line3 in Y1:
    list1.append(line3);
for line2 in Y:
    list.append(line2);
for line4 in list:
    jlists.append(line4);
for line5 in hscore:
    jlists.append(line5);
for line6 in list1:
    jlistn.append(line6);
for line7 in hName:
    jlistn.append(line7);



U = open("Name", "w");
O = open("score", "w");

for e in jlistn:
    U.write(e);
    U.write('\n')
for n in jlists:
    O.write(str(n));
    O.write('\n')



U.close();
O.close();

U = open("Name", "r");
O = open("score", "r");



for x in O:
    sscore.append(int(x));
for x in U:
    sName.append(x.strip('\n'));

#SORTING GOES HERE!
ssscore = [];
ssName = [];

print()

sindex = 0

for x in sscore:
    inserted = False;
    if len(ssscore)==0:
        ssscore.append(x);
        ssName.append(sName[sindex]);
        inserted = True;

    index = 0;
    while index < len(ssscore) and not inserted:
        if ssscore[index] <= x:
            ssscore.insert(index, x);
            ssName.insert(index, sName[sindex]);
            inserted = True;
        index += 1

    if not inserted:
        ssscore.append(x);
        ssName.append(sName[sindex]);
    sindex+=1


while len(ssscore) > 5:
    ssscore.pop(5)
while len(ssName) > 5:
    ssName.pop(5)

if score != 0:
    O = open("score", "w");

    for x in ssscore:
        O.write(str(x));
        O.write('\n');
    O.close();
    U = open("Name", "w");

    for x in ssName:
        U.write(str(x));
        U.write('\n');
    U.close();

else:
    print("You Did Not Get A Score");