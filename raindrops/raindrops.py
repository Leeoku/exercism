def convert(number):
    '''sound = sound1 = sound2 = sound3 = sound4 = ""
    if (int(number) % 3 == 0):
        sound1 = "Pling"
    if (int(number) % 5 == 0):
        sound2 = "Plang"
    if (int(number) % 7 == 0):
        sound3 = "Plong"
    elif (int(number)%3 !=0 and int(number)%5 !=0 and int(number)%7 !=0):
        sound4 = str(number)
    sound = sound1+sound2+sound3+sound4'''
    
    #Alternate solution
    sound = ""
    if int(number) % 3 == 0:
        sound += "Pling"
    if int(number) % 5 == 0:
        sound += "Plang"
    if int(number) % 7 == 0:
        sound += "Plong"
    if sound == "":
        sound = str(number)
    return sound