number = input("Zadej číslo dne: ")
number = int(number)

if number >= 1 and number <= 365:
    reminder = (number-1)%7
    if reminder == 0: 
        day = 1
    if reminder == 1: 
        day = 2
    if reminder == 2: 
        day = 3
    if reminder == 3: 
        day = 4
    if reminder == 4: 
        day = 5
    if reminder == 5: 
        day = 6
    if reminder == 6: 
        day = 7
    if number == 365: 
        day = 1
else:
    day = 0

match day:
    case 1: print("Den v týdnu: neděle")
    case 2: print("Den v týdnu: pondělí")
    case 3: print("Den v týdnu: úterý")
    case 4: print("Den v týdnu: středa")
    case 5: print("Den v týdnu: čtvrtek")
    case 6: print("Den v týdnu: pátek")
    case 7: print("Den v týdnu: sobota")
    case _: print("Chyba: Zadáno špatné číslo, vybírejte z intervalu <1,365>")

if number >= 1 and number <= 365:
    if number >= 1 and number <= 31:
        print("Měsíc: leden")
    if number >= 32 and number <= 59:
        print("Měsíc: únor")
    if number >= 60 and number <= 80:
        print("Měsíc: březen")
    if number >= 81 and number <= 110:
        print("Měsíc: duben")
    if number >= 111 and number <= 141:
        print("Měsíc: květen")
    if number >= 142 and number <= 171:
        print("Měsíc: červen")
    if number >= 172 and number <= 202:
        print("Měsíc: červenec")
    if number >= 203 and number <= 233:
        print("Měsíc: srpen")
    if number >= 234 and number <= 263:
        print("Měsíc: září")
    if number >= 264 and number <= 294:
        print("Měsíc: říjen")
    if number >= 295 and number <= 324:
        print("Měsíc: listopad")
    if number >= 325 and number <= 365:
        print("Měsíc: prosinec")
    
    

