a = int(raw_input("Input the first number: "))
b = int(raw_input("Input the second number: "))
c = int(raw_input("Input the third number: "))
if a <= b and a <=c:
    if b <= c:
        print "The value is " + str(b)
    else:
        print "The value is " + str(c)
else:
    if b <= a and b <= c:
        if a <= c:
            print "The value is " + str(a)
        else:
            print "The value is " + str(c)
    else:
        if b <= c:
            print "The value is " + str(b)
        else:
            print "The value is " + str(c)
