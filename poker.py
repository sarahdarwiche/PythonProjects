import random
def newHand():
    suite=["clubs","diamonds","hearts","spades"]
    value=["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
    deck=[]
    for i in value:
        for b in suite:
            deck.append((i,b))
    random.shuffle(deck)
    hand=(deck[0:5])
    return hand
def cardToValue(card):
    suite={"clubs":0,"diamonds":1,"hearts":2,"spades":3}
    face={"ace":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"10":9,"jack":10,"queen":11,"king":12}
    thisface,thissuite= card
    return face[thisface]*4+suite[thissuite]
def valueToCard(value):
    suite=["clubs","diamonds","hearts","spades"]
    face=["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
    thissuite = value %4
    thisface = value//4
    return face[thisface],suite[thissuite]
def isStraight(hand):
    handValues = []
    for card in hand:
        handValues.append(cardToValue(card)//4)
    if(isStraightValues(handValues)):
        return True
    elif 0 in handValues:
        handValues[handValues.index(0)] = 13
        return isStraightValues(handValues)
    return False
def isStraightValues(handValues):
    handValues.sort()
    for i in range(4):
        if(handValues[i] != (handValues[i+1]-1)):
            return False
    return True
def isFlush(hand):
    (face,suit) = hand[0]
    for card in hand:
        (face,newsuit)= card
        if suit!=newsuit:
            return False
    return True
def pairs(hand):
    pairslist = []
    for card in hand:
        for othercard in hand[hand.index(card)+1:]:
            cardV = cardToValue(card)
            othercardV = cardToValue(othercard)
            if((cardV != othercardV) and (othercardV //4 == cardV //4)):
                pairslist.append((card,othercard))
    
    if len(pairslist)==6:
        return "Four of a Kind"
    elif len(pairslist)==4:
        return "Full House"
    elif len(pairslist)==3:
        return "Three of a Kind"
    elif len(pairslist)==2:
        return "Two Pair"
    elif len(pairslist)==1:
        return "Pair"
    else:
        return "Nothing"
    
def isRoyalFlush(hand):
    if isStraight(hand) and isFlush(hand):
        valueHand = []
        for i in hand:
            valueHand.append(cardToValue(i)//4)
        return 0 in valueHand and 12 in valueHand and True
    return False
def handType(hand):
    pairslist = []
    if isRoyalFlush(hand):
        return "Royal Flush"
    elif isStraight(hand) and isFlush(hand):
        return "Straight Flush"
    elif isFlush(hand):
        return "Flush"
    elif isStraight(hand):
        return "Straight"
    else:
        return pairs(hand)
def highestValue(hand1,hand2):
    values1=[]
    values2=[]
    for card in hand1:
        values1.append(cardvalue(card))
        values1.sort()
    for cards in hand2:
        values2.append(cardvalue(cards))
        values2.sort()
def compare(hand1,hand2):
    values1=[]
    values2=[]
    for card in hand1:
        values1.append(cardToValue(card))
        values1.sort()
    for cards in hand2:
        values2.append(cardToValue(cards))
        values2.sort()
    handTypes=["Royal Flush","Straight Flush","Four of a Kind","Full House","Flush","Straight","Three of a Kind","Two Pair","Pair","Nothing"] 
    x=handTypes.index(handType(hand1))
    y=handTypes.index(handType(hand2))
    if x<y:
        return True
    elif x>y:
        return False
    else:
        if(handTypes[x] == "Straight" or handTypes[x] == "Royal Flush" or handTypes[x] == "Straight Flush"):
            return getStraightRank(values1) > getStraightRank(values2)
        elif(handTypes[x]=="Flush"):
           if getFlushRank(values1) > getFlushRank(values2):
               return True
           else:
                return False
        elif(handTypes[x] == "Full House"):
            if getFullHouseRank(values1)>getFullHouseRank(values2):
                return True
            else:
                return False
        elif (handTypes[x] == "Four of a Kind"):
            if getFourRank(values1) > getFourRank(values2):
                return True
            else:
                return False
        elif (handTypes[x] == "Three of a Kind"):
            if  getThreeRank(values1)>getThreeRank(values2):
                return True
            else:
                return False
        elif (handTypes[x] == "Two Pair"):
            if (getTwoPairRank(values1))>(getTwoPairRank(values2)):
                return True
            else:
                return False
        elif(handTypes[x] == "Pair"):
            if getPairRank(values1)>getPairRank(values2):
                return True
            else:
                return False
        elif values1[4]>values2[4]:
           return True
        else:
            values1[4]==values2[4]
            if values1[3]>values2[3]:
                return True
            else:
                return False
def getStraightRank(values):
    if(min(values) < 4 and max(values) > 47):
        return min(values) +52
    else:
        return max(values)
def getFlushRank(values):
    return (max(values))
def getPairRank(values):
    if values[0]<=values[1]<4:
        return "1"
    else:
        return "0"
def detFourRank(values):
    if values[0]<=values[1]<=values[2]<=values[3]<4:
        return "1"
    else:
        return "0"
def getFullHouseRank(values):
    if min(values)<4:
        return "1"
    else:
        return "0"
def getThreeRank(values):
    if min(values)<4:
        return "1"
    else:
        return "0"
def getTwoPairRank(values):
    if values[0]<=values[1]<4:
        return "1"
    else:
        return "0"
