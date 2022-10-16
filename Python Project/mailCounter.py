fhand=open('file.txt')
wordCount=dict()
for line in fhand:
    word=line[line.find('@')+1:line.find('.')]
    wordCount[word]=wordCount.get(word,0)+1
print(wordCount)