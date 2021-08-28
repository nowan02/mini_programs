#hash
class hash:
    def __init__(self, _ascii):
        self._ascii = _ascii
        self.word = ""
        self.status = "Never used"

#table
hashTable = []
n = 0
while n < 26:
    hashTable.append(hash(97+n))
    n+=1

#printout
def out(table):
    n = 0
    print("---------------------------------------------")
    while n < 26:
        print(table[n].status + " ")
        n+=1
    print("---------------------------------------------")

#program loop
while 1:
    userInput = list(input())
    if len(userInput) < 11:
        if userInput[0] == "A":
            print(userInput[len(userInput)-1])
            i = ord(userInput[len(userInput)-1])-97
            while True:
                if i > 25:
                    i = 0   
                if hashTable[i].status != "Occupied":
                    userInput.remove("A")
                    for letter in userInput:
                        hashTable[i].word += letter
                    hashTable[i].status = "Occupied"
                    out(hashTable)
                    break
                else:
                    if hashTable[i].status != "Occupied":
                        userInput.remove("A")
                        for letter in userInput:
                            hashTable[i].word += letter
                        hashTable[i].status = "Occupied"
                        out(hashTable)
                        break
                if i+1 == ord(userInput[len(userInput)-1])-97:
                    print("no empty slot")
                    break
                i+=1
        if userInput[0] == "D":
            userInput.remove("D")
            lookfor = ""
            for letter in userInput:
                lookfor += letter
            i = ord(userInput[len(userInput)-1])-97
            while True:
                if i > 25:
                    i = 0
                if(hashTable[i].word == lookfor):
                    hashTable[i].word = ""
                    hashTable[i].status = "Tombstone"
                    out(hashTable)
                    break
                if i+1 == ord(userInput[len(userInput)-1])-97:
                    print("word not found")
                    break
                i+=1
        if userInput == "q":
            exit()
    else:
        pass