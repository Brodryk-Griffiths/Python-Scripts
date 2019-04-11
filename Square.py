import math
print "Draw a Square"
edgeSize = (raw_input("Enter a numnber between 10 and 50 :  "))
if edgeSize > 50 or edgeSize < 10:
    print "Can you even read?"
else:


    print "X" * int(edgeSize)
    count = 0
    while count <> (int(edgeSize) / 2):
        pass
        print "X" + " " * (int(edgeSize) - 2) + "X"
        count = count + 1
    print "X" * int(edgeSize)
