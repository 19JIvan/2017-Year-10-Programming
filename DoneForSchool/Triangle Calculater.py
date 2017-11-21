from os import system;
import time;
import math;

D = 1;
P = 0;
Q = 0;
W = 0;
E = 0;
R = 0;
Y = 0;
V1 = 0;
V2 = 0;
V3 = 0;
V4 = 0;


print("Hello I Am Going To Tell You The Answer To Your Trigonometry Question!");
print("To Do This You Need To Tell Me The Information That You Know About The Triangle");
print("Remember! To Just Press Enter When You Dont Know The Information For The Question Given");
time.sleep(2);

while P == 0:
    print("What Is The Unit Of Measurement");
    Measurement = input();
    M = Measurement;
    if M == "km" or M == "m" or M == "cm" or M == "mm" or M == "":
        P = 1;
        Y = 1;
    if M != "km" and M != "m" and M != "cm" and M != "mm" and M != "":
        print("Please Type A Real Unit Of Measurement");
        system("say Please Type A Real Unit Of Measurement");

while Q == 0:
    print("What Is The Theta Of The Triangle");
    Theta = input();
    try:
        T = float(Theta);
    except ValueError:
        T = 0;
        V1 = 1;
    if Theta == "x" or V1 == 0 or Theta == "":
        Q = 1;
    if Theta != "x" and V1 == 1 and Theta != "":
        print("Please Type A Real Theta, Type x Or Hit Enter");

while W == 0:
    print("What Is The Hypotenuse Of The Triangle");
    Hypotenuse = input();
    try:
        H = float(Hypotenuse);
    except ValueError:
        H = 0;
        V2 = 1;
    if Hypotenuse == "x":
        while Y == 0:
            print("What Is The Unit Of Measurement");
            Measurement = input();
            M = Measurement;
            if M == "km" or M == "m" or M == "cm" or M == "mm":
                Y = 1;
            if M != "km" and M != "m" and M != "cm" and M != "mm" and M != "":
                print("Please Type A Real Unit Of Measurement");
    if Hypotenuse == "x" or V2 == 0 or Hypotonuse == "":
        W = 1;
    if Hypotenuse != "x" and V2 == 1 and Hypotenuse != "":
        print("Please Type A Real Hypotenuse, Type x Or Hit Enter");

while E == 0:
    print("What Is The Adjacent Of The Triangle");
    Adjacent = input();
    try:
        A = float(Adjacent);
    except ValueError:
        A = 0;
        V3 = 1;
    if Adjacent == "x":
        while Y == 0:
            print("What Is The Unit Of Measurement");
            Measurement = input();
            M = Measurement;
            if M == "km" or M == "m" or M == "cm" or M == "mm":
                Y = 1;
            if M != "km" and M != "m" and M != "cm" and M != "mm" and M != "":
                print("Please Type A Real Unit Of Measurement");
    if Adjacent == "x" or V3 == 0 or Adjacent == "":
        E = 1;
    if Adjacent != "x" and V3 == 1 and Adjacent != "":
        print("Please Type A Real Adjacent, Type x Or Hit Enter");

while R == 0:
    print("What Is The Opposite Of The Triangle");
    Opposite = input();
    try:
        O = float(Opposite);
    except ValueError:
        O = 0;
        V4 = 1;
    if Opposite == "x":
        while Y == 0:
            print("What Is The Unit Of Measurement");
            Measurement = input();
            M = Measurement;
            if M == "km" or M == "m" or M == "cm" or M == "mm":
                Y = 1;
            if M != "km" and M != "m" and M != "cm" and M != "mm" and M != "":
                print("Please Type A Real Unit Of Measurement");
    if Opposite == "x" or V4 == 0 or Opposite == "":
        R = 1;
    if Opposite != "x" and V4 == 1 and Opposite != "":
        print("Please Type A Real Opposite, Type x Or Hit Enter");

if Theta == "x":
    if Hypotenuse == "":
        ans = math.atan(O / A);
        D = 0;

    elif Adjacent == "":
        ans = math.asin(O / H);
        D = 0;

    else:
        ans = math.acos(A / H);
        D = 0;


if Hypotenuse == "x":
    if Theta == "":  # H, O, A
        ans = math.sqrt(math.pow(O, 2) + math.pow(O, 2));

    elif Adjacent == "":  # H, O, T Sin
        ans = O * math.sin(math.radians(T));

    else:  # H, A, T Cos
        ans = A * math.cos(math.radians(T));

if Adjacent == "x":
    if Theta == "":  # A, H, O
        ans = math.sqrt(math.pow(H, 2) + math.pow(O, 2));

    elif Hypotenuse == "":  # A, O, T Tan
        ans = O * math.tan(math.radians(T));

    else:  # A, H, T Cos
        ans = H * math.cos(math.radians(T));


if Opposite == "x":
    if Theta == "":  # O, H, A
        ans = math.sqrt(math.pow(H, 2) + math.pow(A, 2));

    elif Hypotenuse == "":  # O, A, T Tan
        ans = A * math.tan(math.radians(T));

    else:  # O, H, T Cos
        ans = H * math.cos(math.radians(T));

if D == 0:
    print("%r Degrees" % ans);

if D != 0:
    print(ans, M);
