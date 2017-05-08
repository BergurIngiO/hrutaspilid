#Ísar Daði Pálsson og Bergur Ingi Ólafsson
#07.05.2017
#Lokaverkefni í Forritun
from random import *
from time import *
#Hér er random og time import til að hægja á kóðanum
hrutateljari = 0
teljari1 = 1
flokkur = 0
hrutalisti = []
tolva=[]
spilari1=[]
bord=[]
þyngd = 1
mjolkurlagni_daetra = 2
einkunn_ullar = 3
fjoldi_afkvaema = 4
einkunn_laeris = 5
frjosemi = 6
thykkt_bakvodva = 7
einkunn_fyrir_malir = 8
#Hér eru allar breyturnar fyrir kóðann

with open("hrutar.txt", "r", encoding="utf-8")as f:
    for line in f:
        hrutalisti.append(eval(line))
    #Hér opna ég hrútar.txt til að evala það til að auðvelda mér notkun á hrútalistanum seinna
shuffle(hrutalisti)
#Hér shuffla ég listanum og er kominn með random lista
spilari1.append(hrutalisti[:26])
tolva.append(hrutalisti[26:])
#Hér appenda ég helming og helming til tölvunnar og notandans
while len(spilari1[0])==0 or len(tolva[0]):
    #Á meðan annaðhvort talvan eða spilarinn á enn hrúta, þá heldur þessi lykja áfram að renna
    teljari1+=1
    if teljari1%2==0:
        dicta1 = spilari1[0]
        #Hér skilgreindi ég dicta eitt sem fyrsta tagið í spilari því að fyrsta tagið í spilari 1 er allur listinn
        #Því að þetta varð listi inni í lista útaf enhverjum óþekktum ástæðum
        print("Nú á notandi leik")
        print("Notandi er með hrútinn", dicta1[0].keys())
        print("-------------------------------------------------------------------------------")
        print("Veldu 0 ef þú vilt keppa í þyngd hrútsins.----------------------------",list(dicta1[0].values())[0][0],"KG. \n"
              "Veldu 1 ef þú vilt keppa í mjólkurlagni dætra sem hrúturinn á.--------",list(dicta1[0].values())[0][1],"\n"
              "Veldu 2 ef þú vilt keppa í gæði ullar sem er á hrútnum.---------------",list(dicta1[0].values())[0][2],"\n"
              "Veldu 3 ef þú vilt keppa í fjölda afkvæma sem hrúturinn á.------------",list(dicta1[0].values())[0][3],"\n"
              "Veldu 4 ef þú vilt keppa í gæði lærsins sem hrúturinn hefur.----------",list(dicta1[0].values())[0][4],"\n"
              "Veldu 5 ef þú vilt keppa í frjósemi hrútsins.-------------------------",list(dicta1[0].values())[0][5],"\n"
              "Veldu 6 ef þú vilt keppa í þykkt bakvöðva hrútsins.-------------------",list(dicta1[0].values())[0][6],"\n"
              "Veldu 7 ef þú vilt keppa í gæðum fyrir malir hrútsins.----------------",list(dicta1[0].values())[0][7],"\n")
                                                                                    #Hér sérðu mig skilgreina fyrsta tagið í dicta1
                                                                                    #Og prenta values úr því
        print("-------------------------------------------------------------------------------")
        flokkur=int(input("Sláðu inn tölu til að velja flokk!"))
        #Hér bið ég notandi um að velja hvaða flokk hann vill keppa í
    if teljari1%2==1:
        dicta2 = tolva[0]
        for key, value in dicta2[0].items():
            print("Nú á tölvan leik")
            print("Tölvan er með hrútinn",key)
            print(value)
            #Hér nota ég key og value í dicta2 fyrir tölvuna til að greina úr fyrsta dictionaríinu í listanum
        flokkur = randint(1,8)
        #Talvan velur sjálfkrafa flokk hér
    if flokkur == 0:
        print("Nú verður keppt um hvor hrútur er með meiri þyngd", )
    elif flokkur == 1:
        print("Nú verður keppt um hvor hrútur á dætur með meiri mjólkurlögn")
    elif flokkur == 2:
        print("Nú verður keppt hvor hrútur er með betri ull")
    elif flokkur == 3:
        print("Nú verður keppt um hvor hrútur á fleiri afkvæmi")
    elif flokkur == 4:
        print("Nú verður keppt um hvor hrútur er með betri læri")
    elif flokkur == 5:
        print("Nú verður keppt um hvor hrúturinn er frjósamari")
    elif flokkur == 6:
        print("Nú verður keppt um hvor hrútur er með meiri gæði og þykkt í bakvöðvanum")
    elif flokkur == 7:
        print("Nú verður keppt um hvor hrútur er með betri malir")
    #hér ráðast flokkarnir og svo kemur þriggja sekúnda pása útaf sleep taginu
    dicta2 = tolva[0]
    if flokkur != 0 and flokkur <= 8:
        for key,value in dicta1[0].items():
            print("Notandi er með hrútinn", key)
            print(key,"er með", value[flokkur-1])
            #Hér nota ég tagið flokkur-1 því að values eru frá 1 - 7 og flokkur er frá 1 - 8
            #Þannig í staðinn fyrir að harðkóða þetta eða "Ljótkóða",þá nota ég þetta bara einfaldlega svona
            bord.append(dicta1[0])
            spilari1[0].remove(dicta1[0])
            #Hérna appenda ég fyrsta tagið hjá notandanum í pottinn og set 2 sekúndna pásu
        for key,value in dicta2[0].items():
            print("Tölvan er með hrútinn", key)
            print(key,"er með",value[flokkur-1])
            bord.append(dicta2[0])
            tolva[0].remove(dicta2[0])
            #Þetta er alveg eins og í forlykkjunni á undan, bara tölvan er tekin í gegn
        if list(dicta1[0].values())[0][flokkur] > list(dicta2[0].values())[0][flokkur]:
            #hér er lína sem skilgreinir hvort value er hærra og það skilgreinir hver vinnur0
            print("Notandi hefur unnið")
            print("")
            dicta1 += (bord)
            bord=[]
            #Hér appenda ég í aftur í dicta eða spilari1[0] því að þetta var tvöfaldur listi eins og ég sagði
            #Svo reseta ég bord því að nú er umferðin búin
        elif list(dicta1[0].values())[0][flokkur] < list(dicta2[0].values())[0][flokkur]:
            print("Tölva hefur unnið")
            print("")
            dicta2 += (bord)
            bord = []
            #Nákvæmlega sama og hér að ofan, bara tölvan er tekinn í gegn

        else:
            print("Jafntefli")
            print("Potturinn er með",len(bord),"hrúta.")
            #Hér er potturinn ekki tæmdur ef það er jafntefli

    if flokkur > 7:
        print("Þú verður að velja flokk til að keppa í, gerðu aftur!")
        teljari1-=1
        #Hér er látið notanda gera aftur ef hann skildi velja vitlaust

    print("Notandi er með", len(spilari1[0]),"hrúta")
    print("Tölvan er með", len(tolva[0]),"hrúta")
    print("")
    #Hér er prentað stöðu leiksins

    if len(spilari1[0]) == 0:
        print("Notandi hefur tapað öllum hrútunum sínum")
        print("Tölvan hefur unnið með", len(tolva[0]), "hrúta")
        print("SKYNET!!!!")
        #Ef spilarinn tapar öllum hrútunum á gerist þetta
        break

    elif len(tolva[0]) == 0:
        print("Tölvan hefur tapað öllum hrútunum sínum")
        print("Notandi hefur unnið með",len(spilari1[0]))
        print("SKYNET IS NO MORE!!!!!")
        #ef talvan tapar öllum hrútunum sínum, þá gerist þetta
        break
