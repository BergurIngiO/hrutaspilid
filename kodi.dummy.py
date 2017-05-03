# Ísar Daði Pálsson og Bergur Ingi Ólafsson
# 2?.04.2017
# Lokaverkefni í Forritun
from random import *

teljari = 1
hrutateljari = 0
teljari1 = 2
kostur = "ja"
talnalisti = []
flokkur = 0
þyngd = 1
mjolkurlagni_daetra = 2
einkunn_ullar = 3
fjoldi_afkvaema = 4
einkunn_laeris = 5
frjosemi = 6
thykkt_bakvodva = 7
einkunn_fyrir_malir = 8
player = []
computer =[]
spilin = []

while kostur == "ja":
    teljari1 += 1
    if teljari1 % 2 == 0:
        # teljari1+=1
        print("nú á notandi leik")
        flokkur = int(input("Sláðu inn tölu"))
    if teljari1 % 2 == 1:
        # teljari1+=1
        print("nú á tölvan leik")
        flokkur = randint(1, 8)
    if flokkur == 1:
        print("Nú verður keppt um hvor hrútur er með meiri þyngd")
    if flokkur == 2:
        print("Nú verður keppt um hvor hrútur er á dætur með meiri mjólkurlögn")
    if flokkur == 3:
        print("Nú verður keppt hvor hrútur er með betri ull")
    if flokkur == 4:
        print("Nú verður keppt um hvor hrútur á fleiri afkvæmi")
    if flokkur == 5:
        print("Nú verður keppt um hvor hrútur er með betri læri")
    if flokkur == 6:
        print("Nú verður keppt um hvor hrúturinn er frjósamari")
    if flokkur == 7:
        print("Nú verður keppt um hvor hrútur er með meiri gæði og þykkt í bakvöðvanum")
    if flokkur == 8:
        print("Nú verður keppt um hvor hrútur er með betri malir")

    else:
        print("Þú verður að velja flokk til að keppa í")

    with open("hrutar.txt", "r", encoding="utf-8")as f:
        texti = f.read()
        texti2 = texti.split(";")
        # print(texti2[randint(0,52)])
        for x in range(len(texti2)):
            print("---------------------------------------------------------------------------------")
            print(teljari)
            print(texti2[hrutateljari])
            teljari += 1
            hrutateljari += 1
            if hrutateljari == len(texti2):
                hrutateljari = 0
        teljari = 0
 
    input("Viltu halda áfram? ja/nei")
