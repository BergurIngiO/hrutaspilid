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
þyngd = 1
mjolkurlagni_daetra = 2
einkunn_ullar = 3
fjoldi_afkvaema = 4
einkunn_laeris = 5
frjosemi = 6
thykkt_bakvodva = 7
einkunn_fyrir_malir = 8

with open("hrutar.txt", "r", encoding="utf-8")as f:
    texti = f.read()
    texti2 = texti.split(";")
for x in range(len(texti2)):
    hrutalisti.append(texti2[hrutateljari])
    hrutateljari += 1
shuffle(hrutalisti)
flag=True
for i in range(len(texti2)):
    while len(hrutalisti)>0 and flag==True:
        teljari2 += 1
        if teljari2 % 2 == 0:
            spilari1.append(hrutalisti[0])
        if teljari2 % 2 == 1:
            tolva.append(hrutalisti[0])
            flag = False
dicta1 = eval(spilari1[0])
dicta2 = eval(tolva[0])
while kostur == "ja":
    teljari1+=1
    if teljari1%2==0:
        for key, value in dicta1.items():
            print("nú á notandi leik")
            print("Notandi er með hrútinn", key)
            print("Veldu 1 ef þú vilt keppa í þyngd hrútsins.\n",value[0],"KG. \n"
                  "Veldu 2 ef þú vilt keppa í mjólkurlagni dætra sem hrúturinn á.\n",value[1],"\n"
                  "Veldu 3 ef þú vilt keppa í gæði ullar sem er á hrútnum.\n",value[2],"\n"
                  "Veldu 4 ef þú vilt keppa í fjölda afkvæma sem hrúturinn á.\n",value[3],"\n"
                  "Veldu 5 ef þú vilt keppa í gæði lærsins sem hrúturinn hefur.\n",value[4],"\n"
                  "Veldu 6 ef þú vilt keppa í frjósemi hrútsins.\n",value[5],"\n"
                  "Veldu 7 ef þú vilt keppa í þykkt bakvöðva hrútsins.\n",value[6],"\n"
                  "Veldu 8 ef þú vilt keppa í gæðum fyrir malir hrútsins.\n",value[7],"\n")
            flokkur=int(input("Sláðu inn tölu til að velja flokk!"))
    if teljari1%2==1:
        for key, value in dicta2.items():
            print("nú á tölvan leik")
            print("Tölvan er með hrútinn",key)
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


    if flokkur != 0 and flokkur <= 8:
        print("calm your pussy")





    if spilari1 == False or tolva == False:
        print("búið")


    else:
        print("Þú verður að velja flokk til að keppa í, gerðu aftur!")
        teljari1-=1

    kostur=input("Viltu halda áfram?")
    sleep(3)
