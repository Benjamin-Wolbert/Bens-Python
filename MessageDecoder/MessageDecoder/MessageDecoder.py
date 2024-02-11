# Programmer: Benjamin Wolbert
# Date: 02/09/2024 (mm/dd/yyyy)
# Last Edited: 02/10/2024
# Program Name : Message Decoder
# Purpose: Take a written file and decode a message from provided numbers and words 
# (which are from a pyramid formation)
# Warning: I am not a python dev so this may be rocky
# 1
# 23
# 456





def Decode(fileName):
    message = ""
    maxnum = 0;
    solutionSet = [""]
    index=1
    with open(fileName) as fileObject:
        for line in fileObject:
         emptyPosition = int(line.find(" "))
         position = int(line[:emptyPosition])
         if position>maxnum:
            maxnum = position 
        while index <= maxnum:
            solutionSet.append("")
            index = index + 1 
    with open(fileName) as fileObject:
        for line in fileObject:
         emptyPosition = int(line.find(" "))
         position = int(line[:emptyPosition])
         
         word = line[emptyPosition+1:]
         solutionSet[position] = word
         if position>maxnum:
            maxnum = position
    index = 1
    step = 1
    # print(solutionSet[0] +" " + solutionSet [6])
    while index<maxnum:
       message = message + solutionSet[index-1] + " "
       # print("before change: " + str(index))
       index+=step
       step+=1
       # print("after change: " + str(index))
       # print(str(step))
    message = message + solutionSet[maxnum]
    return message

      

print(Decode('message_file.txt'))
                
# numandword = input("num + space + word\n")
# emptyPosition = int(numandword.find(" "))
# position = int(numandword[:emptyPosition])
         
# word = numandword[emptyPosition+1:]

# print (word + " " + str(position))