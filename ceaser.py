from string import maketrans, translate

alphabet = "abcdefghijklmnopqrstuvwxyz"

def brute_force() :
    code = raw_input("Enter your code text: ")

    for offset in range (26) :

        ceaser = alphabet[offset:] + alphabet[0:offset]

        trans = maketrans(alphabet, ceaser)
                             
        print translate(code, trans)

def encode() :
    offset = 10
    ceaser = alphabet[offset:] + alphabet[0:offset]

    trans = maketrans(alphabet, ceaser)
                             
    phrase = raw_input("Enter your plaintext phrase: ")

    print translate(phrase, trans)

answer = raw_input("(encode) or (break) a Code?: ")

if answer == "break" :
    brute_force()
else : 
    encode()
