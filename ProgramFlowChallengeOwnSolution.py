# TIM BUCHALKA'S AND JEAN-PAUL ROBERTS' COMPLETE PYTHON MASTERCLASS AT WWW.UDEMY.COM
#
# START OF CHALLENGE FOR PROGRAM FLOW IN PYTHON                                                                                                                                                       # plus all additionals, each showing the addition name, and addition price, and a grand/final total for the
# Create a program that takes an IP address entered the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop.
# But your program should just count however many are entered
# 127.0.0.1
# .192.168.0.1
# 10.0.123456.255
# 172.16
#
# So your program should work even with invalid IP Addresses. We're just interested
# in the number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
# .123.45.678.91
# 123.4567.8.9
# 10.10t.10.10
# 12.9.34.6.12.90
# '' - that is, press enter without typing anything
# This challenge is intended to practice for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.
#
# END OF CHALLENGE FOR PROGRAM FLOW IN PYTHON
#
#      link to the Complete Python Masterclass of Tim Buchalka and Jean-Paul Roberts at udemy.com:
#      https://www.udemy.com/python-the-complete-python-developer-course/
#
# START OF MY OWN SOLUTION

# Definition of variables
segmentLength = 0
actualSegment = 1
IPAddress = str(input('Enter an IP address: '))
dotCounter = 0

# Validation of input data
for char in IPAddress:
    if char not in '0123456789.':
        print("X", end='') # replacing invalid characters with "X"
    else:
        print(char, end='')
print("")


for char in IPAddress:
    if char not in '0123456789.':
        print(char, end='') #printing invalid characters in the same position
    else:
        if char == ".":
            print(char, end='') # dots are printed to show the position of invalid character
        else:
            print(' ', end='') # valid characters are hidden. the goal is to show the invalid character with their position
print("")

for i in range (0, len(IPAddress)):
    if IPAddress[i] == '.':
        dotCounter += 1

if dotCounter > 3:
    print("Too many dots (and segments): {} ({})".format(dotCounter, dotCounter+1))
else:
    if dotCounter < 3:
        print("Not enough dots (and segments): {} ({})".format(dotCounter, dotCounter+1))

if (IPAddress != '') and (IPAddress[0] == "."): # If input was empty '', it would lead to error. So an extra condition must have been added.
    print("The first character should no be dot!")

if (IPAddress != '') and (IPAddress[-1] == "."): # If input was empty '', it would lead to error. So an extra condition must have been added.
    print("The last character should no be dot!")

# Counting length of segments
if IPAddress == '':
    print('The IP Address is empty!')
else:
    for i in range (0, len(IPAddress)):
        if IPAddress[i] == '.':
            print("Segment {} with length {}".format(actualSegment, segmentLength))
            segmentLength = 0
            actualSegment += 1
            continue
        segmentLength += 1
    print("Segment {} with length {}".format(actualSegment, segmentLength))







