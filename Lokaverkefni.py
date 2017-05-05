#Ísar Daði Pálsson og Bergur Ingi Ólafsson
#2?.04.2017
#Lokaverkefni í Forritun
from random import *
from time import *
teljari = 1
hrutateljari = 0
teljari1 = 1
teljari2 = 1
kostur = "ja"
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

with open("hrutar.txt", "r", encoding="utf-8")as f:
    for line in f:
        hrutalisti.append(eval(line))
shuffle(hrutalisti)
spilari1.append(hrutalisti[:26])
tolva.append(hrutalisti[26:])
while len(spilari1[0])==0 or len(tolva[0]):
    teljari1+=1
    if teljari1%2==0:
        dicta1 = spilari1[0]
        #for key, value in dicta1.items():
        print("Nú á notandi leik")
        print("Notandi er með hrútinn", spilari1[0][0].keys())
        print("-------------------------------------------------------------------------------")
        print("Veldu 1 ef þú vilt keppa í þyngd hrútsins.----------------------------",list(spilari1[0][0].values())[0][0],"KG. \n"
              "Veldu 2 ef þú vilt keppa í mjólkurlagni dætra sem hrúturinn á.--------",list(spilari1[0][0].values())[0][1],"\n"
              "Veldu 3 ef þú vilt keppa í gæði ullar sem er á hrútnum.---------------",list(spilari1[0][0].values())[0][2],"\n"
              "Veldu 4 ef þú vilt keppa í fjölda afkvæma sem hrúturinn á.------------",list(spilari1[0][0].values())[0][3],"\n"
              "Veldu 5 ef þú vilt keppa í gæði lærsins sem hrúturinn hefur.----------",list(spilari1[0][0].values())[0][4],"\n"
              "Veldu 6 ef þú vilt keppa í frjósemi hrútsins.-------------------------",list(spilari1[0][0].values())[0][5],"\n"
              "Veldu 7 ef þú vilt keppa í þykkt bakvöðva hrútsins.-------------------",list(spilari1[0][0].values())[0][6],"\n"
              "Veldu 8 ef þú vilt keppa í gæðum fyrir malir hrútsins.----------------",list(spilari1[0][0].values())[0][7],"\n")
        print("-------------------------------------------------------------------------------")
        flokkur=int(input("Sláðu inn tölu til að velja flokk!"))
    if teljari1%2==1:
        dicta2 = tolva[0]
        for key, value in dicta2[0].items():
            print("Nú á tölvan leik")
            print("Tölvan er með hrútinn",key)
            print(value)
            sleep(2)
        flokkur = randint(1,8)
    if flokkur == 1:
        print("Nú verður keppt um hvor hrútur er með meiri þyngd", )
        sleep(3)
    elif flokkur == 2:
        print("Nú verður keppt um hvor hrútur á dætur með meiri mjólkurlögn")
        sleep(3)
    elif flokkur == 3:
        print("Nú verður keppt hvor hrútur er með betri ull")
        sleep(3)
    elif flokkur == 4:
        print("Nú verður keppt um hvor hrútur á fleiri afkvæmi")
        sleep(3)
    elif flokkur == 5:
        print("Nú verður keppt um hvor hrútur er með betri læri")
        sleep(3)
    elif flokkur == 6:
        print("Nú verður keppt um hvor hrúturinn er frjósamari")
        sleep(3)
    elif flokkur == 7:
        print("Nú verður keppt um hvor hrútur er með meiri gæði og þykkt í bakvöðvanum")
        sleep(3)
    elif flokkur == 8:
        print("Nú verður keppt um hvor hrútur er með betri malir")
        sleep(3)

    dicta2 = tolva[0]
    if flokkur != 0 and flokkur <= 8:
        for key,value in dicta1[0].items():
            print("Notandi er með hrútinn", key)
            print(key,"er með", value[flokkur-1])
            bord.append(dicta1[0])
            spilari1[0].remove(dicta1[0])
            sleep(2)
        for key,value in dicta2[0].items():
            print("Tölvan er með hrútinn", key)
            print(key,"er með",value[flokkur-1])
            bord.append(dicta2[0])
            tolva[0].remove(dicta2[0])
            sleep(2)
        if list(dicta1[0].values())[0][flokkur - 1] > list(dicta2[0].values())[0][flokkur - 1]:
            print("Notandi hefur unnið")
            print(bord)
            spilari1[-1].append(bord)

        elif list(dicta1[0].values())[0][flokkur - 1] < list(dicta2[0].values())[0][flokkur - 1]:
            print("Tölva hefur unnið")
            print(bord)
            tolva[-1].append(bord)
        else:
            print("Jafntefli")

    if flokkur == 0 or flokkur > 8:
        print("Þú verður að velja flokk til að keppa í, gerðu aftur!")
        teljari1-=1

    print("Notandi er með", len(spilari1[0]),"hrúta")
    print("Tölvan er með", len(tolva[0]),"hrúta")
    sleep(3)

if len(spilari1[0]) == 0:
    print("Notandi hefur tapað öllum hrútunum sínum")
    print("Tölvan hefur unnið með", len(tolva), "hrúta")
    print("SKYNET!!!!")


elif len(tolva[0]) == 0:
    print("Tölvan hefur tapað öllum hrútunum sínum")
    print("Notandi hefur unnið með",len(spilari1))
    print("SKYNET IS NO MORE!!!!!")
