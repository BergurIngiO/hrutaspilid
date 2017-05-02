#Ísar Daði Pálsson og Bergur Ingi Ólafsson
#2?.04.2017
#Lokaverkefni í Forritun
from random import *
from time import *
teljari = 1
hrutateljari = 0
teljari1 = 1
kostur = "ja"
flokkur = 0
hrutalisti = []
tolva=[]
spilari1=[]
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
    if teljari1%2==1:
        print("nú á tölvan leik")
        flokkur = randint(1,8)
    if flokkur == 1:
        print("Nú verður keppt um hvor hrútur er með meiri þyngd")
        sleep(3)
    elif flokkur == 2:
        print("Nú verður keppt um hvor hrútur er á dætur með meiri mjólkurlögn")
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

    if flokkur != 0 and flokkur <= 8:
        with open("hrutar.txt", "r", encoding="utf-8")as f:
            texti = f.read()
            texti2 = texti.split(";")
            for x in range(len(texti2)):
                hrutalisti.append(texti2[hrutateljari])
                hrutateljari += 1
                teljari += 1

            if hrutateljari == len(texti2):
                hrutateljari = 0
                teljari = 1

            #hrutalisti.remove('\n')
            print(hrutalisti)

            dicta=eval(hrutalisti[0])
        for key,value in dicta.items():
            print(key)



    else:
        print("Þú verður að velja flokk til að keppa í, gerðu aftur!")
        teljari1-=1

    kostur=input("Viltu halda áfram?")
    sleep(3)
