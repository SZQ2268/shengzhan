import sys
print("you really run this bad Code?")
print("you pc has dired!")
really = input("(y/n)")
number = 2
if really == "y" or really == "Y":
    while True:
        number = number ** 2
        print("number is ",number)
elif really == "n" or really == "N":
    print("well you Survival !")
    sys.exit(0)
else:
    print("fuck you")
    sys.exit(0)