sentence = input ("Please enter your sentence\n").upper()

listOfWord = sentence.split()
sentences = sentence.replace(" ","")
listOfWords = list(sentences)

dict ={}
listdict={}

for words in listOfWord:

     if words not in dict:

         dict[words]=1


     else:

        dict [words]+=1
        
for words in listOfWords:
    
     if words not in listdict:

         listdict[words]=1


     else:

        listdict[words]+=1



print ("\nWords frequency: ", dict)
print ("\nLetter frequency: ",listdict)