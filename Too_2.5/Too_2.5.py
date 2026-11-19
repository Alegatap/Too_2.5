print("Vali programm:\n"
    "1 - Arvu kontroll\n"
    "2 - Kehamassiindeks\n"
    "3 - Ostu allahindlus\n")
try:
    valik=int(input(""))
    if valik == 1:
        print("Arvu kontroll")    # oli print('Arvu kontroll"), paredasin ' --> "          
        try:                                        # lisa try/except sest me provime sissesta täisarv
            arv=int(input("Sisesta täisarv => "))   # oli "str" type, lisa int() sest me tahame täisarv
            if arv>0:                               # : pudusin, oli if arv>0
                print("Arv on positiivne")
            else:                                   # : pudusin pärast else. If oli saama riida oli nagu  else if arv=0:
                if arv==0:                          # oli if arv=0:  ainult üks =. 
                    print("Arv on null")            # oli vali koht, lisa veel üks TAB
                else:                               # oli vale koht, lisa veel üks TAB
                    print("Arv on negatiivne")      # vale koht, lisa kaks TAB
            if arv%2==0:                            
                print("Arv on paarisarv")
            else:
                print("Arv on paaritu")
            if arv % 3 == 0:            # tehtud, et prograam kontrolib, kas asv jagub 3-ga
                print("arv jagub 3-ga")
            else: print("arv ei jagub 3-ga")
        except: print("sissesta ainult täisarv")  
    elif valik == 2:
        print("kehamassiindeks")
        try:                                              #try sest me provime sissesta arv
            mass=float(input("sisesta kaal (kg) => "))
            pikkus=float(input("sisesta pikkus (m) => ")) # üks ) pudub
            print(mass,pikkus)
            if mass <= 0 or pikkus <= 0: # lisaülesanne, et see ei saa olema negatiivne või 0
                print("Negatiivne/null maas või pikkus ei sobi") 
            else:
                kmi=round(mass/pikkus*2,1) #panesin round siin, see on paremini
                print("kmi:", kmi)         # kustasin ära round siin

                if 0 < kmi <18.5:         #kmi ei saa olema negatiivne, see ei ole logiline
                    print("alakaal")
                elif 18.5 <= kmi < 25:          #panasin siin kõik et kõik valikud on praegu täpselt
                    print("normaalkaal")
                elif 25 <= kmi < 30:
                    print("ülekaal")
                elif 30 <= kmi:               #siin ei panasinud "else" sest elif ka töötab
                    print("rasvumine")
        except: print("palun sissesta ainult numbrid")
    elif valik == 3:
        print("Ostu allahindlus")
        try:                    #TRY sest provime sissesta numbrid
            summa=round(float(input("Sisesta ostusumma => ")),2) #panasin siin ka round sest me kasutame summa hiljem ja seal ei ole round
            if summa<=0:            #oli =< see on vale, õige on <=
                print("Vigane summa")
            elif 100 < summa <500:                                #oli loogiline viga, oli summa>100 or summa<=500: see tähendab
                print("Allahindlus 5%, maksta:", round(summa*0.95,2))    #et kui summa on 1, siis sa ka Allahindlus 5%, aga valik ütleb, et kui summa < 100
            elif summa>=500: #tehtud et summa >=500 sest oli logic viga  #siis Allahindlust pole
                print("Allahindlus 10%, maksta:", round(summa*0.9,2))
            else:                           # : pärast ELSE pudub
                print("Allahindlust pole, maksta:", summa) # ) lõppus pudub
        except: print("sissesta ainult numbrid")
    else: print("valik ei leidnud")
except: print("Vigane valik") 

# print()

#Programmi tulemus:

# Arvu kontroll
# Sisesta täisarv => 9
# Arv on positiivne
# Arv on paaritu

# Kehamassiindeks
# Sisesta kaal (kg) => 85
# Sisesta pikkus (m) => 1.75
# KMI: 27.8
# Ülekaal

# Ostu allahindlus
# Sisesta ostusumma => 650
# Allahindlus 10%, maksta: 585.0
# Lisaülesanne:

# Muuda programmi nii, et alguses kuvatakse menüü ja kasutaja valib, millist osa käivitada:
 
# Vali programm:
# 1 - Arvu kontroll
# 2 - Kehamassiindeks
# 3 - Ostu allahindlus
# Sisesta valik (1-3) =>
# Käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.

# Lisa arvu kontrolli osasse kontroll, kas arv jagub 3-ga.
# Kehamassiindeksi osa ei tohi lubada sisestada nulli või negatiivset kaalu või pikkust.
# Lisaülesande tulemus (näide):

 
# Vali programm:
# 1 - Arvu kontroll
# 2 - Kehamassiindeks
# 3 - Ostu allahindlus
# Sisesta valik (1-3) => 1
# Arvu kontroll
# Sisesta täisarv => 9
# Arv on positiivne
# Arv on paaritu
# Arv jagub 3-ga
