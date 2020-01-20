import sys
import time
#Recept: https://www.ica.se/recept/pannkakor-grundsmet-2083/
#
#Det som krävs
#----------------------------------
minMilk = 6 #Minst mjölk som krävs dl
minFlour = 250 #Minsta mjöl gram
minEggs = 3 #Minsta ägg som krävs
#----------------------------------
#Slut

print ('Välkommen!\nDetta är en maskin som räknar ut hur många pannkakor du kan göra.\nVänligen skriv bara in siffor i svarsrutorna.')
time.sleep(2) #Väntar 2 sekunder
print ('För att kunna göra pannkakor behöver du:')
time.sleep(2)
print ('6dl mjölk')
time.sleep(1)
print ('250gram mjöl')
time.sleep(1)
print ('3 ägg')
time.sleep(3)

       
#Hur mycket av sakerna har du?
#----------------------------------
#Hur mycket mjölk har du?
print('Hur många dl mjölk har du?')
amountMilk = int(input()) #Skriv in hur mycket mjölk du har
#Slut

#Hur mycket mjöl har du?
print('Hur mycket mjöl har du? Svara i gram')
amountFlour = int(input()) #Skriv in hur mycket mjölk du har
#Slut

#Hur många ägg har du?
print('Hur många ägg har du?')
amountEggs = int(input()) #Skriv in hur många ägg du har
#Slut
#----------------------------------

#Kod
if amountFlour < minFlour or amountEggs < minEggs or amountMilk < minMilk:
    print('Du kan inte laga pannkakor :(')
else:
    #Uträkning
    #-------------------------------------
    #Mjöl
    amountFlour = amountFlour // minFlour
    print('Du har ' + str(amountFlour) + 'portioner mjöl')
    #Ägg
    amountEggs = amountEggs // minEggs
    print('Du har ' + str(amountEggs) + 'portioner ägg')
    #Mjölk
    amountMilk = amountMilk // minMilk
    print('Du har ' + str(amountMilk) + 'portioner mjölk')

    #Vilken är den minsta?
    smallest = 1
    if amountEggs <= amountMilk and amountMilk <= amountFlour:
        smallet = amountEggs
    elif amountFlour <= amountMilk and amountFlour <= amountEggs:
        smallest = amountFlour    
    else:
        smallest = amountMilk

    print(' ') #Varje portion är 8 pannkakor
    print('Du kan laga ' + str(smallest*8) + 'pannkakor')
    #Hur mycket behöver du?
    print (' ')
    print ('Du behöver ' + str(smallest*minEggs) + ' ägg')
    print ('Du behöver ' + str(smallest*minFlour) + ' gram mjöl')
    print ('Du behöver ' + str(smallest*minMilk) + ' dl mjölk')
    #-------------------------------------
