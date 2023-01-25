
import time    # Importation du module time
import msvcrt  # Ce module (facultatif) nous permettra de sortir de la boucle en préssant la bare-espace

def intervalle_heure():
    while True:    # création d'une boucle while qui s'executera tant que True == True
        import datetime
        now = datetime.datetime.now()
        print ("Il est actuellement : ")
        print (now.strftime("%H:%M:%S"))
        time.sleep(1)    # intervalle d'une seconde

        if msvcrt.kbhit(): #Si nous pressons bare-espace ...
                if ord(msvcrt.getch()) == 32:
                    break                               #... nous sortons de la boucle

intervalle_heure()

def afficher_heure(heures, minutes, secondes):
    import datetime
    now = datetime.datetime.now()

    print("Original time:", now.strftime("%H:%M:%S"))

    modified_time = now.replace(hour=heures, minute=minutes, second=secondes)

    print(modified_time.strftime("%H:%M:%S"))
    print("Modified time:", modified_time.strftime("%H:%M:%S"))

afficher_heure(15, 15, 15)


# FAIL

def regler_alarme(heures, minutes, secondes):
    import datetime 
    now = datetime.datetime.now()

    while True:
        
        if (heures != now.strftime("%H") , minutes != now.strftime("%M") , secondes != now.strftime("%S")):
            None
        else : 
            print("Dring Dring")


#regler_alarme(16, 10, 50)
