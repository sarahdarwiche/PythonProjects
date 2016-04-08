file = open("starfile.txt", 'r')
dictStar = {}

def starSetup():
    for line in file:
        splitLine = line.split()
        dictStar[splitLine[0]]=float(splitLine[1]),float(splitLine[2])

def starData(starName):
    if starName in dictStar:
        return dictStar[starName]
    else:
        return('Not found')
    
def starDistance(low,high):
    for i in dictStar:
        distance, AVM = dictStar[i]
        if low<distance<high:
            print(i)

def starAVM(low,high):
    for i in dictStar:
        distance, AVM = dictStar[i]
        if low<AVM<high:
            print(i)
            
def starMeans(dictStar):
    acc=bcc=ccc=dcc=ecc=fcc=0
    G0 = []
    G1 = []
    G2 = []
    G3 = []
    G4 = []
    G5 = []
    for i in dictStar:
        distance, AVM = dictStar[i]
        if 0.0<AVM<=0.5:
            acc = acc + distance
            G0.append(i)
        elif 0.5<AVM<=1.0:
            bcc = bcc + distance
            G1.append(i)
        elif 1.0<AVM<=1.5:
            ccc =  ccc + distance
            G2.append(i)
        elif 1.5<AVM<=2.0:
            dcc = dcc + distance
            G3.append(i)
        elif 2.0<AVM<=2.5:
            ecc = ecc + distance
            G4.append(i)
        elif 2.5<AVM<=3.0:
            fcc = fcc + distance
            G5.append(i)
    print("The mean distance of the stars in dictStar with 0.0<AVM<=0.5 is", (acc/len(list(G0))))
    print("The mean distance of the stars in dictStar with 0.5<AVM<=1.0 is", (bcc/len(list(G1))))
    print("The mean distance of the stars in dictStar with 1.0<AVM<=1.5 is", (ccc/len(list(G2))))
    print("The mean distance of the stars in dictStar with 1.5<AVM<=2.0 is", (dcc/len(list(G3))))
    print("The mean distance of the stars in dictStar with 2.0<AVM<=2.5 is", (ecc/len(list(G4))))
    print("The mean distance of the stars in dictStar with 2.5<AVM<=3.0 is", (fcc/len(list(G5))))
