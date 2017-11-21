from operator import itemgetter
import copy
import time

Dic = {}
list = []
list1 = []
TempFixtureList = []
TempFixtureList1 = []
FixtureList = []
M = 0
Matches = 0
LOOP = "FOREVER"
NAME = ""
LOOP1 = "FOREVER"

O = open("CS:GO/CS:GO PLACES", "r")
for x in O:
     x = x.strip('\n')
     list1.append(x)
O.close()




while LOOP1 == "FOREVER":
    print("Do You Want To Enter Teams 'Manually' Or Get The Teams And Scores From The Save 'File'")
    PCNT = input()

    if PCNT == "Manually" or PCNT == "manually":
        CN = int(input("Enter How Many CS:GO Teams Are In The Tournament"))

        print("Enter The Names Of Each CS:GO Teams One By One")
        time.sleep(0.25)
        for index in range(0, CN):
            CNT = input("Enter The Teams Name")
            SCNT = input("Enter The Teams Tag")
            list.append([CNT, 0, 0, 0, 0]) #([Name, Score, Wins, Losses, Byes])
            Dic[CNT] = SCNT
            print(Dic)

        for e in list:
            NAME = Dic.get(e[0])
            CNT = int(input("Enter The Score For Team " +str(NAME)))
            e[1] += CNT

        for b in list:
            NAME = Dic.get(b[0])
            #Q = list.index(b)
            print()
            WIN = input("Did " + str(NAME) + " 'Win', 'Loss' Or Had A 'Bye'")
            print()
            if WIN == "Win" or WIN == "win":
                b[2] += 1
            if WIN == "Loss" or WIN == "loss":
                b[3] += 1
            if WIN == "Bye" or WIN == "bye":
                b[4] += 1


        MA = int(input("How Many Matches Have Been Played Overall"))
        Matches += int(MA)

        list.sort(key=itemgetter(1), reverse=True)
        LOOP1 = "BREAK"

    else:
        print()

    if PCNT == "File" or PCNT == "file":
        P = open("CS:GO/CS:GO LADDER", "r")
        I = open("CS:GO/CS:GO DIC", "r")
        U = open("CS:GO/CS:GO MATCHES", "r")
        for Line in I:
            Line = Line.strip('\n')
            Abbreviations, Name = Line.split(':')
            Dic[Abbreviations] = Name
        for Line in P:
            Line = Line.strip('\n')
            Name, Score, Wins, Losses, Byes = Line.split(',')
            list.append([Name, int(Score), int(Wins), int(Losses), int(Byes)])
        for Line in U:
            Matches = Line
        P.close()
        I.close()
        U.close()
        print(list)
        LOOP1 = "BREAK"
    else:
        print()



while LOOP == "FOREVER":

    C = input("Would You Like To Show 'Ladder' Or Enter The Match 'Results'"
              " Or Create A 'Fixture' For Next Round Or Do You Want To 'Save' The Ladder") #This Is The Menu

    print()
    if C == "Ladder" or C == "ladder":
        while M < len(list):
            e = list[M]
            print()
            print("The "+str(e[0])+" Are In "+str(list1[M])+" Place With A Score Of "+str(e[1])+" Points And Have Won "+str(e[2])+", Lost "+str(e[3])+" And Had "+str(e[4])+" Byes")
            print()
            M += 1
        print("The Overall Matches That Have Been Played Is "+str(Matches))
        C = input("Would You Like To Enter The Scores, Wins And Losses For The Lastest Matches")

    print()

    if C == "Results" or C == "results" or C == "Yes" or C == "yes":
        if TempFixtureList == []:
            for e in list:
                CNT = int(input("Enter The Score For Team " + str(e[0])))
                e[1] += CNT
            for a in list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       :
                NAME = Dic.get(a[0])
                #Q = list.index(a[0])
                print()
                WIN = input("Did "+str(NAME)+" 'Win', 'Lose' Or Had A 'Bye'")
                print()
                if WIN == "Win" or WIN == "win":
                    a[2] += 1
                if WIN == "Lose" or WIN == "lose":
                    a[3] += 1
                if WIN == "Bye" or WIN == "bye":
                    a[4] += 1

        if TempFixtureList != []:
            for a in list:
                NAME = Dic.get(a[0])
                CNT = int(input("Enter The Score For Team " + str(NAME)))
                a[1] += CNT
            for e,a in zip(TempFixtureList, list)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       :
                NAME = Dic.get(e[0])
                NAME1 = Dic.get(e[1])
                Q = list.index(e[0])
                W = list.index(e[1])
                print()
                WIN = input("Did "+str(NAME)+" 'Win', 'Lose' Or Had A 'Bye'")
                print()
                LOSE = input("Did "+str(NAME1)+" 'Win', 'Lose' Or Had A 'Bye'")
                print()
                if WIN == "Win" or WIN == "win":
                    Q[2] += 1
                if WIN == "Lose" or WIN == "lose":
                    Q[3] += 1
                if WIN == "Bye" or WIN == "bye":
                    Q[4] += 1
                if LOSE == "Win" or LOSE == "win":
                    W[2] += 1
                if LOSE == "Lose" or LOSE == "lose":
                    W[3] += 1
                if LOSE == "Bye" or WIN == "bye":
                    W[4] += 1


        list.sort(key=itemgetter(1), reverse=True)
        MA = input(Matches+" Is How Many Matches Have Been Played Enter How Many More Matches Have Been Played")
        Matches += int(MA)

    if C == "Fixture" or C == "fixture":

        for a in list:
            FixtureList.append(a[0])
            print(FixtureList)

        while len(FixtureList) != 0:

            A = FixtureList.pop()

            FixtureList.reverse()

            if len(FixtureList) > 0:

                B = FixtureList.pop()

                FixtureList.reverse()

            if B == None:
                TempFixtureList1.append(A)

            if B != None:
                Q = (A, B)

                TempFixtureList.append(Q)
            B = None


        for e in TempFixtureList:
            NAME = Dic.get(e[0])
            NAME1 = Dic.get(e[1])
            print()
            print(str(NAME)+" Is Versing "+str(NAME1))
            print()

        if len(TempFixtureList1) != 0:
            NAME = Dic.get(TempFixtureList1[0])
            print()
            print(str(NAME)+" Has A Bye")
            print()

    if C == "Save" or C == "save":
        P = open("CS:GO/CS:GO LADDER", "w")
        I = open("CS:GO/CS:GO DIC", "w")
        U = open("CS:GO/CS:GO MATCHES", "w")
        for N in Dic:
            I.write(N+':'+str(Dic[N])+'\n')
        for N in list:
            P.write(N[0]+','+str(N[1])+','+str(N[2])+','+str(N[3])+','+str(N[4])+'\n')
        U.write(str(Matches))
        P.close()
        I.close()
        U.close()