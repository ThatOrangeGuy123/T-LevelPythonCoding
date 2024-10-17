#Define Function
def timestables(NumOut):
    #Enter Loop of 5 increments
    for i in range(0,5):
        #Double the Number
        NumOut = int(NumOut) * 2
        #Output the result
        print(NumOut)
#User Inputs Initial Number
UserNumber = input("Enter a Number: ")
#Call Function
timestables(UserNumber)