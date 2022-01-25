introduction = input("Give your Introduction: ")
#print(introduction)
chcount= 0
wordcount = 1
for i in introduction:
    chcount = chcount+1
    if(i == " "):
        wordcount = wordcount+1
print("No. of words in the string: ")
print(wordcount)

print("No. of characters in the string: ")
print(chcount)