sentence=input("Enter Your Sentence: ")
print(sentence)
wordCount=1
charCount=0
for i in sentence:
    charCount=charCount+1
    if(i==' '):
        wordCount=wordCount+1
print('Number of Words in the Sentence: ', wordCount)
print('Number of Characters in the Sentence: ', charCount)