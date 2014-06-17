from string import maketrans, translate

alphabet = "abcdefghijklmnopqrstuvwxyz"

offset = 10
ceaser = alphabet[offset:] + alphabet[0:offset]

trans = maketrans(alphabet, ceaser)
                         
phrase = raw_input("Enter your plaintext phrase: ")

print translate(phrase, trans)
