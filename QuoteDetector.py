def quoteDetector(input):
    inputSplit = input.split()
    occurrence = []
    finalString = ""
    output = []
    flag = False
    for i in range(0, len(inputSplit)):
        if inputSplit[i].startswith("“") or inputSplit[i].endswith("”"):
            if inputSplit[i].startswith("“") and inputSplit[i].endswith("”"):
                output.append(inputSplit[i])
            occurrence.append(i)
    if len(occurrence) == 2:
        flag = True
    if flag:
        for i in range(occurrence[0], occurrence[1] + 1):
            finalString += inputSplit[i] + " "
        finalString = finalString[:-1]
        output.append(finalString)
    if len(output) > 0:
        return output
def main():
    file = open("stave1.txt", mode="r", encoding='UTF8')
    STAVE = file.read()
    PARAGRAPHS = STAVE.split('\n')
    listOfQuotes = []
    for i in PARAGRAPHS:
        x = quoteDetector(i)
        if x!= None:
            for i in x:
                listOfQuotes.append(i)
    return listOfQuotes

print(main())
