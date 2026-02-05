# cti 110
# P1LAB1
# Andrew Worth
# 2/5/2026
# pratice Python program

# name = "Big Daddy"
# greet the user

first_name = input(("Hi, whats your first name?"))
last_name = input(("Hi, whats your last name?"))

print ("nice to meet you",first_name, last_name)
print () # extra blank line
hobby = input("whats type of 'stuff'do you like?")
print( "I am a Computer but i would probably like ", hobby, "too" )

# example of a loop
print("i cant repeat myself!")
count = int(input("how many times should i repeat?"))
for time in range(count):
    print("i know a song that drives poeple crazy,")