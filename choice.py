
print "Hi!"

name = raw_input("What is your name?: ")
answer = raw_input("Do you like (hot) or (cold)?: ");

if answer == "hot" :
    print name + " would be happy on a beach in the Caribbean"
elif answer == "cold" :
    print "Maybe " + name + " should go and live in an igloo"
elif answer == "clod" :
    print "I think " + name + " is a bit of a clod too"
else :
    print "That is not an answer I (or anyone) recognises"
