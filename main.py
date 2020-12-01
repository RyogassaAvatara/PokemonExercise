import re



def sequence(file_name):
    with open(file_name, 'r') as p:
        file = re.findall('\w+', p.read())
    current = []
    longest = []

    def letters(last_l, tempList):
        for i in tempList:
            if i.startswith(last_l):
                return tempList.index(i)
        return False


    for name in file:
        currentName = name
        current.append(currentName)
        dupList = file
        dupList.pop(dupList.index(currentName))
        index = letters(currentName[-1], dupList)

        while index is not False:
            currentName = dupList[index]
            current.append(currentName)
            dupList.pop(index)
            index = letters(currentName[-1], dupList)

        if len(current) > len(longest):
            longest = current

        current = []

    return longest

print(sequence('pokemon.txt'))






