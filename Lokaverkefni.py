#Ísar Daði Pálsson og Bergur Ingi Ólafsson
#2?.04.2017
#Lokaverkefni í Forritun
from random import *
teljari = 1
hrutateljari = 0
teljari1 = 1
teljari2=0
kostur = "ja"
flokkur = 0
talnalisti = []
þyngd = 1
mjolkurlagni_daetra = 2
einkunn_ullar = 3
fjoldi_afkvaema = 4
einkunn_laeris = 5
frjosemi = 6
thykkt_bakvodva = 7
einkunn_fyrir_malir = 8

while kostur == "ja":
    teljari1+=1
    if teljari1%2==0:
        print("nú á notandi leik")
        print("Veldu 1 ef þú vilt keppa í þyngd hrútsins.\n"
              "Veldu 2 ef þú vilt keppa í mjólkurlagni dætra sem hrúturinn á.\n"
              "Veldu 3 ef þú vilt keppa í gæði ullar sem er á hrútnum.\n"
              "Veldu 4 ef þú vilt keppa í fjölda afkvæma sem hrúturinn á.\n"
              "Veldu 5 ef þú vilt keppa í gæði lærsins sem hrúturinn hefur.\n"
              "Veldu 6 ef þú vilt keppa í frjósemi hrútsins.\n"
              "Veldu 7 ef þú vilt keppa í þykkt bakvöðva hrútsins.\n"
              "Veldu 8 ef þú vilt keppa í gæðum fyrir malir hrútsins.\n")
        flokkur=int(input("Sláðu inn tölu til að velja flokk!"))
    if teljari1%2==1 or teljari2 == 3:
        print("nú á tölvan leik")
        flokkur = randint(1,8)
    if teljari2 == 3:
        print("Þú valdir vitlaust 4 sinnum þannig að nú færðist valrétturinn yfir til tölvunnar!")
        teljari2 = 0
        teljari1=1
    if flokkur == 1:
        print("Nú verður keppt um hvor hrútur er með meiri þyngd")
    elif flokkur == 2:
        print("Nú verður keppt um hvor hrútur er á dætur með meiri mjólkurlögn")
    elif flokkur == 3:
        print("Nú verður keppt hvor hrútur er með betri ull")
    elif flokkur == 4:
        print("Nú verður keppt um hvor hrútur á fleiri afkvæmi")
    elif flokkur == 5:
        print("Nú verður keppt um hvor hrútur er með betri læri")
    elif flokkur == 6:
        print("Nú verður keppt um hvor hrúturinn er frjósamari")
    elif flokkur == 7:
        print("Nú verður keppt um hvor hrútur er með meiri gæði og þykkt í bakvöðvanum")
    elif flokkur == 8:
        print("Nú verður keppt um hvor hrútur er með betri malir")

    if flokkur != 0 and flokkur <= 8:
        with open("hrutar.txt", "r", encoding="utf-8")as f:
            texti = f.read()
            texti2 = texti.split(";")
            for x in range(len(texti2)):
                print("---------------------------------------------------------------------------------")
                print(teljari)
                print(texti2[hrutateljari])
                teljari+=1
                hrutateljari+=1
                if hrutateljari == len(texti2):
                    hrutateljari=0
            teljari=1
    else:
        print("Þú verður að velja flokk til að keppa í, gerðu aftur!")
        teljari1-=1
        teljari2+=1
        
    input("Viltu halda áfram? ja/nei")




