def createWordsList(filename):
    data = [line.strip() for line in open(filename,'r')]
    return data
def CanWeMakeIt(myWord,myLetters):
    W = list(myWord)
    L = list(myLetters)
    for i in W:
        if i in L:
            L.remove(i)
        else:
            return(False)
    return(True)
letterPoints = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
def getWordPoints(myWord,letterPoints):
    acc = 0
    for i in myWord:
        lettervalue = letterPoints[i] 
        acc = acc + lettervalue
    return acc
def scrabbleWords(myLetters):
    WordList = createWordsList('wordlist.txt')
    myWords = []
    for i in WordList:
        if CanWeMakeIt(i,myLetters) == True:
            myWords.append(i)
    myWordPoints = {}
    for i in myWords:
        myWordPoints[i]=getWordPoints(i,letterPoints)
        pointWordList = []
    for i in myWordPoints:
        pointvalue = myWordPoints[i]
        word = i
        tup = (pointvalue,word)
        pointWordList.append(tup)
        pointWordList.sort()
        pointWordList.reverse()
    for i in pointWordList:
        print('%s %d' % (i[1].ljust(len(myLetters)+4),i[0]))
    file = open('%s' % (myLetters) + 'txt', 'w')
    for i in pointWordList:
        file.write('%s %d' % (i[1].ljust(len(myLetters)+4),i[0]) + '\n')
    file.close
        

    

            
        
        
        
