# -*- coding: utf-8 -*-
import fonctionJeuNoel
                           
continuer = 0
if continuer == 0:
                                                
    level = 1
    att = 3
    deff = 1
    pvmax = 5
    pv = pvmax
    xpmax = 10
    xp = 0
    po = 5
    attmag = 0
    deffmag = 0
    pm = 0
    
    stat = dict()  
    stat['PV'] = pv
    stat['level'] = level
    stat['xp'] = xp
    stat['PO'] = po
    stat['att'] = att
    stat['def'] = deff
    stat['att magique'] = attmag
    stat['def magique'] = deffmag
    stat['PM'] = pm

    print("Tu vas devoir choisir ta classe !")
    print("Il y a 4 classes qui on toute un avantage :")
    print("- guerrier : il a plus d'att et de def")
    print("- mage : il a une att magique")
    print("- le soigneur : peut utiliser des sort de soin")
    # print("- alchimiste : peut faire des potions de force") # je sais pas comment faire
    
    classe = raw_input("quelle classe veus tu incarner ?")
    stat['classe'] = classe
    
    if (classe == 'guerrier'):
        print("Tu es maintenant un guerrier.")
        att = att + 1
        deff = deff + 1
        print(stat)
    elif classe == 'mage':
        print("Tu es maintenant un mage.")
        pm = pm + 10
        attmag = attmag + 3            
        deffmag = deffmag + 1
        print(stat)
        capacite = fonctionJeuNoel.capacitemage
    elif classe == 'soigneur':
        print("tu es maintenant un soigneur.")
        print("Tu peut soigner de 3PV")
        pm = pm + 10
        print(stat)
        capacite = fonctionJeuNoel.capacitesoigneur 
    elif classe == 'cerise':
        print("Bravo tu a trouver une classe speciale")
        print("Cette classe te diminu la quantite d'XP a avoir c'est super non ?")
        
    print("nouvelle sauvegarde")
    print("'nouvelle sauvegarde' permet de passer à l'etape suivante. Pour cela, tu dois taper dans la terminal où je te parle : [continuer = save]")
    
    continuer = 1
    
if continuer == 1:
    while pv > 0:
        print("Bonjour")
        print("Tu vas incarner un heros.")
        r1 = raw_input("Commencons tout de suite ! Reponds par [oui]  pour commencer.")
        if (r1 == 'oui'):
            print("Tu es attaque(e)")
            attenemy = 2
            deffenemy = 0
            pvenemy = 3
            print(stat['PV'])
            fonctionJeuNoel.combat (pv, att, deff, pvenemy, attenemy, deffenemy, capacite)
            
            xp = xp + 5
            po = po + 2
            print("Avec [stat[stat en question]] tu peut voir la stat que tu veux")
    
        print("fin")
        continuer == 2
    else:            
        print("Tu es mort(e)")