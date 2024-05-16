alphadict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def constructGrid():

    grid = [[alphabet[(j+i) % 26] for j in range(26)] for i in range(26)]

    return grid

def printGrid(grid):

    for i in range(26):
        print(grid[i])

def getMessageSpacing(message):

    spaces = []
    for i in range(len(message)):
        if (message[i] == ' '):
            spaces.append(i)

    return spaces

def alignThem(message, key):

    alignDict = []
    messageLength = len(message)
    keyLength = len(key)

    for i in range(messageLength):
        alignDict.append((message[i], key[i % keyLength]))

    return alignDict

def enrypt(grid, messageKey, spaces):

    encryptedMessage = ""
    messageLength = len(messageKey)
    spacePointer = 0
    pointerNo = 0

    for i in range(messageLength):

        if spacePointer <= len(spaces) - 1:
            if i == spaces[spacePointer] - pointerNo:
                spacePointer += 1
                pointerNo += 1
                encryptedMessage += " "

        tuple = messageKey[i]
        encryptedMessage += grid[alphadict[tuple[0]]][alphadict[tuple[1]]]

    return encryptedMessage


def playGame():
    key = input("Please input the key: ")
    key = "".join(key.split())

    message = input("Please input the message: ")
    spaces = getMessageSpacing(message)
    message = "".join(message.split())

    grid = constructGrid()

    messageKey = alignThem(message, key)

    encryptedMessage = enrypt(grid, messageKey, spaces)


    printGrid(grid)
    print("")
    print(encryptedMessage)

playGame()

# print(alignThem("THIS IS THE EME", "HELLO"))
# print(getMessageSpacing("THIS IS THE EME"))

