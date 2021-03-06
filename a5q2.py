# Bhavana Samudrala
# student number- 11258695
# NSID- bhs053
# Instructor- Arlin Schaffel
# CMPT-145-L14

import Queue as Q
q = Q.Queue()

good_guy = {"Godzilla": [], "Mothra": []}

filename = input("Enter your TestCase or file name: ")
textFile = open(filename, "r")
for x in textFile:
    list = x.strip('\n')

    if list != "Godzilla" and list != "Mothra" :
        q.enqueue(list)
    else:
        good_guy[list].append(q.dequeue())

if q.is_empty():
    print("won the battle - saviours saved the earth")
    for x in good_guy["Godzilla"]:
        print(x)
    for x in good_guy["Mothra"]:
        print(x)
else:
    print("lost the battle - space monsters win")

textFile.close()



