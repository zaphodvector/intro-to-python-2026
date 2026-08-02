"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week11_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-07
    Purpose:	The purpose of this program is to define a Fruit class that will be used 
                to create individual fruit objects.  The fruit class will have attributes
                for FruitName, FruitColor, FruitWeight, and whether or not the fruit needs to
                be peeled.  The program wil then show constructing and manipulating instances
                of the fruit object.  The program will also review previously learned material.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-07	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random
class EVW_Fruit:
    '''This is the base class for a any type of fruit.  It has attributes for
    strFruitName, strFruitColor, blnNeedsPeeling, and fltFruitWeightInOunces.  It
    also has a print method defined to produce formatted output about a fruit object.
    '''
    def __init__(self, strName="Unknown", strColor="Unknown", \
                 blnNeedsPeeling=False, fltFruitWeightInOunces=0.0):
        self.strFruitName = strName
        self.strFruitColor = strColor
        self.blnNeedsPeeling = blnNeedsPeeling
        self.fltFruitWeightInOunces = fltFruitWeightInOunces

    def __str__(self):
        strFruitPrinted = f"Fruit Name: {self.strFruitName}\tFruit Color: {self.strFruitColor}\n"
        strFruitPrinted += f"  Weight (oz.): {self.fltFruitWeightInOunces}\t"
        strFruitPrinted += f"  Needs Peeling?:{self.blnNeedsPeeling}"
        return strFruitPrinted

def main():
    strMessage = "This program will create a fruit stand by instantiating multiple instances\n"
    strMessage += "  of the EVW_Fruit class and storing these pieces of fruit in a list.\n"
    strMessage += "Let's start off by building 2 specific pieces of fruit. For the first fruit,\n"
    strMessage += "  we will create an 'empty' fruit by passing no parameters for the __init__\n"
    strMessage += "  constructor to use.  Then, we will call the __str__ method to see what\n"
    strMessage += "  the fruit looks like at this point."
    fncPauseAndReflect(strMessage)

    fruitStand = []
    fruitStand.append(EVW_Fruit())
    strMessage = 'The Fruit Stand has been created and initialized empty and a single,\n'
    strMessage += 'blank piece of fruit has been added.  Here is the fruit stand right now.'
    fncPauseAndReflect(strMessage)
    fncShowFruitStand(fruitStand)

    strMessage = "Now, we will update the 'blank' first fruit by setting it's values\n"
    strMessage += "  We will make this a red apple that weighs 4.25 oz.\n"
    strMessage += "  Then, we will re-show the Fruit Stand."
    fruitStand[0].strFruitName = 'Apple'
    fruitStand[0].strFruitColor = 'Red'
    fruitStand[0].fltFruitWeightInOunces = '4.25'
    fncPauseAndReflect(strMessage)
    fncShowFruitStand(fruitStand)

    strMessage = "Next, we will create our new 2nd fruit by setting it's values.\n"
    strMessage += "  at the time we create the object by passing appropriate values.\n"
    strMessage += "  Our 2nd fruit will be a Yellow Banana weighing 3.8 oz."
    fruitStand.append(EVW_Fruit('Banana','Yellow',True,3.8))
    fncPauseAndReflect(strMessage)
    fncShowFruitStand(fruitStand)

    strMessage = "Next, we will create several (10 - 30) random fruits with random properties.\n"
    strMessage += "  The fruits will be either Apples, Bananas, Oranges, or Melons.\n"
    strMessage += "  If the fruits are Bananas, Oranges, or Melons, then they need to be peeled.\n"
    strMessage += "  Bananas can be colored: green, yellow, or brown.  Apples can be\n"
    strMessage += "  colored: green, red, or yellow.  Melons can be colored: orange or green.\n"
    strMessage += "  All weights will be random between 5.0 and 15.0 oz."
    fncPauseAndReflect(strMessage)

    intHowManyFruits = random.randint(10,30)      # how many new fruits
    print(f'The produce folx delivered {intHowManyFruits} pieces of fruit today!')
    for i in range(intHowManyFruits):
        strThisFruitName = random.choice(['Apple','Banana','Orange','Melon'])
        fltThisFruitWeight = round(random.uniform(5.0,15.0),2)
        match strThisFruitName:
            case 'Apple':
                strThisFruitColor = random.choice(['Red','Green','Yellow'])
                blnThisFruitPeels = False
            case 'Orange':
                strThisFruitColor = 'Orange'
                blnThisFruitPeels = True
            case 'Banana':
                strThisFruitColor = random.choice(['Green','Yellow','Brown'])
                blnThisFruitPeels = True
            case 'Melon':
                strThisFruitColor = random.choice(['Orange','Green'])
                blnThisFruitPeels = True
        fruitStand.append(
            EVW_Fruit(strThisFruitName,strThisFruitColor,blnThisFruitPeels,fltThisFruitWeight)
            )
    fncShowFruitStand(fruitStand)
    fncPauseAndReflect()

    strMessage = "Finally, let's discover some information about our fully-stocked Fruit Stand:\n"
    dictSummaryInfo = {}
    for frtSingleFruit in fruitStand:
        strThisFruitName = frtSingleFruit.strFruitName
        fltThisFruitWeight = frtSingleFruit.fltFruitWeightInOunces

        if strThisFruitName not in dictSummaryInfo:     # this is the first fruit of this type
            dictSummaryInfo[strThisFruitName] = {'frtCount':0, 'totWeight':0}  # initialize vars

        dictSummaryInfo[strThisFruitName]['frtCount'] += 1  # update to count one more
        dictSummaryInfo[strThisFruitName]['totWeight'] += float(fltThisFruitWeight)  # update for weight
    strMessage += " Our fully stocked fruit stand now has:\n"
    for frtType in dictSummaryInfo:
        strMessage += f"{frtType:^10}:  Count: {str(dictSummaryInfo[frtType]['frtCount']):>3}  "
        strMessage += f"Weighing: {dictSummaryInfo[frtType]['totWeight']:>5.2f}   "
        strMessage += f"Avg. Weight: {dictSummaryInfo[frtType]['totWeight']/
                                          dictSummaryInfo[frtType]['frtCount']:>5.2f}\n"
    strMessage += ('-' * 80) + "\n"
    intTotalFruitCount = sum(fruitType['frtCount'] for fruitType in dictSummaryInfo.values())
    fltTotalFruitWeight = sum(fruitType['totWeight'] for fruitType in dictSummaryInfo.values())
    strMessage += f"{'Totals':^10}:  Count: {intTotalFruitCount:>3}  "
    strMessage += f"Weight: {fltTotalFruitWeight:>7.2f}   "
    strMessage += f"Avg. Weight: {fltTotalFruitWeight / intTotalFruitCount:>5.2f}\n"
    fncPauseAndReflect(strMessage)


def fncPauseAndReflect(strMessage='',sep='-',rpt=80):
    '''This function first creates a separator string then shows the message passed in.
    Then, the function pauses until the user presses the enter key.
    '''
    print(sep * rpt)
    print(strMessage)
    input('Press the Enter Key to continue...')

def fncShowFruitStand(fruitStand):
    '''This function receives a fruit stand (list of EVW_Fruit objects) and
    iterates through to print the full list.  This function prints the fruit directly
    so this will use the EVW_Fruit's __str__ method.
    '''
    for index, frtSingleFruit in enumerate(fruitStand):
        print(f'Fruit #{index + 1:0>3}:')
        print(frtSingleFruit)

if __name__ == '__main__':
    main()