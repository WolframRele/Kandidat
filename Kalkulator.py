import pywer
import numpy as np
from collections import Counter
from weighted_levenshtein import lev, osa, dam_lev
from Levenshtein import editops
Phones = []
Phonesafr = []
Phonesarg = []
Phonesaze = []
Phonesbos = []
Phonesenguk = []
Phonesengus = []
Phonesepo = []
Phonesest = []
Phoneseus = []
Phonesfin = []
Phonesfraquebec = []
Phonesgrn = []
Phonesina = []
Phonesind = []
Phonesjam = []
Phonesitzlu = []
Phonesmlt = []
Phonesmri = []
Phonesnob = []
Phonesorm = []
Phonespap = []
Phonesque = []
Phonesslk = []
Phonesspa = []
Phonesspamexico = []
Phonessqi = []
Phonesswa = []
Phonestuk = []
Phonestur = []
Phonesuzb = []
Phonesviec = []
Phonesvien = []
Phonesvies = []
Phonesunk = []
LangD = {}
wrongslist = []
levenstinedistance = []
levenstinedistanceafr = []
levenstinedistancearg = []
levenstinedistanceaze = []
levenstinedistancebos = []
levenstinedistanceenguk = []
levenstinedistanceengus = []
levenstinedistanceepo = []
levenstinedistanceest = []
levenstinedistanceeus = []
levenstinedistancefin = []
levenstinedistancefraquebec = []
levenstinedistancegrn = []
levenstinedistanceina = []
levenstinedistanceind = []
levenstinedistancejam = []
levenstinedistanceitzlu = []
levenstinedistancemlt = []
levenstinedistancemri = []
levenstinedistancenob = []
levenstinedistanceorm = []
levenstinedistancepap = []
levenstinedistanceque = []
levenstinedistanceslk = []
levenstinedistancespa = []
levenstinedistancespamexico = []
levenstinedistancesqi = []
levenstinedistanceswa = []
levenstinedistancetuk = []
levenstinedistancetur = []
levenstinedistanceuzb = []
levenstinedistanceviec = []
levenstinedistancevien = []
levenstinedistancevies = []
levenstinedistanceunk = []
weightedlevenshteind = []
weightedlevenshteindafr = []
weightedlevenshteindarg = []
weightedlevenshteindaze = []
weightedlevenshteindbos = []
weightedlevenshteindenguk = []
weightedlevenshteindengus = []
weightedlevenshteindepo = []
weightedlevenshteindest = []
weightedlevenshteindeus = []
weightedlevenshteindfin = []
weightedlevenshteindfraquebec = []
weightedlevenshteindgrn = []
weightedlevenshteindina = []
weightedlevenshteindind = []
weightedlevenshteindjam = []
weightedlevenshteinditzlu = []
weightedlevenshteindmlt = []
weightedlevenshteindmri = []
weightedlevenshteindnob = []
weightedlevenshteindorm = []
weightedlevenshteindpap = []
weightedlevenshteindque = []
weightedlevenshteindslk = []
weightedlevenshteindspa = []
weightedlevenshteindspamexico = []
weightedlevenshteindsqi = []
weightedlevenshteindswa = []
weightedlevenshteindtuk = []
weightedlevenshteindtur = []
weightedlevenshteinduzb = []
weightedlevenshteindviec = []
weightedlevenshteindvien = []
weightedlevenshteindvies = []
weightedlevenshteindunk = []
test = int()
Word = ""
WER = 0
total = 0
totalafr = 0
totalarg = 0
totalaze = 0
totalbos = 0
totalenguk = 0
totalengus = 0
totalepo = 0
totalest = 0
totaleus = 0
totalfin = 0
totalfraquebec = 0
totalgrn = 0
totalina = 0
totalind = 0
totaljam = 0
totalitzlu = 0
totalmlt = 0
totalmri = 0
totalnob = 0
totalorm = 0
totalpap = 0
totalque = 0
totalslk = 0
totalspa = 0
totalspamexico = 0
totalsqi = 0
totalswa = 0
totaltuk = 0
totaltur = 0
totaluzb = 0
totalviec = 0
totalvien = 0
totalvies = 0
totalunk = 0
Error = 0
Errorafr = 0
Errorarg = 0
Erroraze = 0
Errorbos = 0
Errorenguk = 0
Errorengus = 0
Errorepo = 0
Errorest = 0
Erroreus = 0
Errorfin = 0
Errorfraquebec = 0
Errorgrn = 0
Errorina = 0
Errorind = 0
Errorjam = 0
Erroritzlu = 0
Errormlt = 0
Errormri = 0
Errornob = 0
Errororm = 0
Errorpap = 0
Errorque = 0
Errorslk = 0
Errorspa = 0
Errorspamexico = 0
Errorsqi = 0
Errorswa = 0
Errortuk = 0
Errortur = 0
Erroruzb = 0
Errorviec = 0
Errorvien = 0
Errorvies = 0
Errorunk = 0
#Här väljer man vad man vill att den genomsnittliga distansen ska vara (den kommer representeras av 1).
WightAvriger = 4.24126389646
#Här skapas alla vikter för levensteinavståndet.
#--------------------------------------------------
insert_costs = np.ones(128, dtype=np.float64)
delete_costs = np.ones(128, dtype=np.float64)
substitute_costs = np.ones((128, 128), dtype=np.float64)
substitute_costs2 = np.ones((128, 128), dtype=np.float64)  
Distance = open("TruDistance.txt", "r", encoding= "utf-8")
for line in Distance:
    caracters,vector = line.split("	")
    #print(caracters + " " + vector[:-1])
    A,B = caracters.split(",")
    #print(A + " " + B)
    substitute_costs2[ord(A), ord(B)] = (float(vector)/WightAvriger)
    substitute_costs2[ord(B), ord(A)] = (float(vector)/WightAvriger)
#------------------------------------------------------------------------
#Här väljer man vilken data man vill kolla på.
Gesses = ("Resultafr.txt","Resultarg.txt","Resultaze.txt","Resultbos.txt","Resulteng-uk.txt","Resulteng-us.txt","Resultepo.txt","Resulteus.txt","Resultfin.txt","Resultfra-quebec.txt","Resultgrn.txt","Resultina.txt","Resultind.txt","Resultjam.txt","Resultltz-lu.txt","Resultmlt.txt","Resultmri.txt","Resultnob.txt","Resultorm.txt","Resultpap.txt","Resultque.txt","Resultslk.txt","Resultspa.txt","Resultspa-mexico.txt","Resultsqi.txt","Resultswa.txt","Resulttuk.txt","Resulttur.txt","Resultvie-c.txt","Resultvie-n.txt","Resultvie-s.txt")

#Här hämtas all data man vill kolla på in.
#-----------------------------------------------
for file in Gesses:
    Results = open(file, "r", encoding= "utf-8")
    ResultL = []
    guideL = {}
    for i,line in enumerate(Results):
        if i % 2 == 0:
            Word = line[:-1]
        else:
            ResultL.append((Word,line[1:-1]))         
    Results.close
#------------------------------------------------

# Här Hämtas facit in.
#---------------------------------------------------------
    Word = ""
    if file == "Resultafr.txt":
       guide = open("guidewfafr.txt", "r", encoding= "utf-8")
    elif file == "Resultarg.txt":
        guide = open("guidewfarg.txt", "r", encoding= "utf-8")
    elif file == "Resultaze.txt":
        guide = open("guidewfaze.txt", "r", encoding= "utf-8")
    elif file == "Resultbos.txt":
        guide = open("guidewfbos.txt", "r", encoding= "utf-8") 
    elif file == "Resulteng-uk.txt":
        guide = open("guidewfeng-uk.txt", "r", encoding= "utf-8")
    elif file == "Resulteng-us.txt":
        guide = open("guidewfeng-us.txt", "r", encoding= "utf-8") 
    elif file == "Resultepo.txt":
        guide = open("guidewfepo.txt", "r", encoding= "utf-8") 
    elif file == "Resultest.txt":
        guide = open("guidewfest.txt", "r", encoding= "utf-8") 
    elif file == "Resulteus.txt":
        guide = open("guidewfeus.txt", "r", encoding= "utf-8") 
    elif file == "Resultfin.txt":
        guide = open("guidewffin.txt", "r", encoding= "utf-8") 
    elif file == "Resultfra-quebec.txt":
        guide = open("guidewffra-quebec.txt", "r", encoding= "utf-8") 
    elif file == "Resultgrn.txt":
        guide = open("guidewfgrn.txt", "r", encoding= "utf-8") 
    elif file == "Resultina.txt":
        guide = open("guidewfina.txt", "r", encoding= "utf-8") 
    elif file == "Resultind.txt":
        guide = open("guidewfind.txt", "r", encoding= "utf-8") 
    elif file == "Resultjam.txt":
        guide = open("guidewfjam.txt", "r", encoding= "utf-8") 
    elif file == "Resultltz-lu.txt":
        guide = open("guidewfltz-lu.txt", "r", encoding= "utf-8") 
    elif file == "Resultmlt.txt":
        guide = open("guidewfmlt.txt", "r", encoding= "utf-8") 
    elif file == "Resultmri.txt":
        guide = open("guidewfmri.txt", "r", encoding= "utf-8") 
    elif file == "Resultnob.txt":
        guide = open("guidewfnob.txt", "r", encoding= "utf-8") 
    elif file == "Resultorm.txt":
        guide = open("guidewform.txt", "r", encoding= "utf-8") 
    elif file == "Resultpap.txt":
        guide = open("guidewfpap.txt", "r", encoding= "utf-8") 
    elif file == "Resultque.txt":
        guide = open("guidewfque.txt", "r", encoding= "utf-8") 
    elif file == "Resultslk.txt":
        guide = open("guidewfslk.txt", "r", encoding= "utf-8") 
    elif file == "Resultspa.txt":
        guide = open("guidewfspa.txt", "r", encoding= "utf-8") 
    elif file == "Resultspa-mexico.txt":
        guide = open("guidewfspa-mexico.txt", "r", encoding= "utf-8") 
    elif file == "Resultsqi.txt":
        guide = open("guidewfsqi.txt", "r", encoding= "utf-8") 
    elif file == "Resultswa.txt":
        guide = open("guidewfswa.txt", "r", encoding= "utf-8") 
    elif file == "Resulttuk.txt":
        guide = open("guidewftuk.txt", "r", encoding= "utf-8") 
    elif file == "Resulttur.txt":
        guide = open("guidewftur.txt", "r", encoding= "utf-8") 
    elif file == "Resultuzb.txt":
        guide = open("guidewfuzb.txt", "r", encoding= "utf-8")
    elif file == "Resultvie-c.txt":
        guide = open("guidewfvie-c.txt", "r", encoding= "utf-8") 
    elif file == "Resultvie-n.txt":
        guide = open("guidewfvie-n.txt", "r", encoding= "utf-8") 
    elif file == "Resultvie-s.txt":
        guide = open("guidewfvie-s.txt", "r", encoding= "utf-8")
    else:
        guide = open("guidewf.txt", "r", encoding= "utf-8")
    for i,line in enumerate(guide):
        words = line.split("	")
        guideL[words[0]] = words[1][:-1]
#-------------------------------------------------------------------------
    #Kollar om resultatet och fasitet är lika långt (har aldrig förekommit).
    if len(guideL) == len(ResultL):
        print("True")
    else:
        print("False" + " " +  str(len(guideL)) + " " + str(len(ResultL)))
        # Tar fram levenstinevärdet, PER, WER och vilka fel som görs.
        #-------------------------------------------------------
        for gese in ResultL:
            if gese[0] in guideL.keys():
                total = total + 1
                ld = (lev(gese[1].replace(" ",""), guideL[gese[0]].replace(" ",""), insert_costs, delete_costs, substitute_costs))
                wld = ((lev(gese[1].replace(" ",""), guideL[gese[0]].replace(" ",""), insert_costs, delete_costs, substitute_costs2)))
                p = (len(guideL[gese[0]]))
                levenstinedistance.append(ld)
                weightedlevenshteind.append(wld)
                Phones.append(p)
                change = editops(gese[1].replace(" ",""), guideL[gese[0]].replace(" ",""))
                for difrace in change:
                    if difrace[0] == "delete":
                        add = "+" +  gese[1].replace(" ","")[difrace[1]]
                        wrongslist.append(add)
                    if difrace[0] == "insert":
                        add = "-" + guideL[gese[0]].replace(" ","")[difrace[2]]
                        wrongslist.append(add)
                    if difrace[0] == "replace":
                        add = gese[1].replace(" ","")[difrace[1]] + guideL[gese[0]].replace(" ","")[difrace[2]]
                        wrongslist.append(add)
                if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                    Error = Error + 1
                #---------------------------------------------------------------------------

                # Tar fram PER och WER för alla språk.
                #--------------------------------------------------------
                if file == "Resultafr.txt":
                    totalafr = totalafr + 1
                    levenstinedistanceafr.append(ld)
                    weightedlevenshteindafr.append(wld)
                    Phonesafr.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorafr = Errorafr + 1
                if file == "Resultarg.txt":
                    totalarg = totalarg + 1
                    levenstinedistancearg.append(ld)
                    weightedlevenshteindarg.append(wld)
                    Phonesarg.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorarg = Errorarg + 1
                if file == "Resultaze.txt":
                    totalaze = totalaze + 1
                    levenstinedistanceaze.append(ld)
                    weightedlevenshteindaze.append(wld)
                    Phonesaze.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroraze = Erroraze + 1
                if file == "Resultbos.txt":
                    totalbos = totalbos + 1
                    levenstinedistancebos.append(ld)
                    weightedlevenshteindbos.append(wld)
                    Phonesbos.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorbos = Errorbos + 1
                if file == "Resulteng-uk.txt":
                    totalenguk = totalenguk + 1
                    levenstinedistanceenguk.append(ld)
                    weightedlevenshteindenguk.append(wld)
                    Phonesenguk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorenguk = Errorenguk + 1
                if file == "Resulteng-us.txt":
                    totalengus = totalengus + 1
                    levenstinedistanceengus.append(ld)
                    weightedlevenshteindengus.append(wld)
                    Phonesengus.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorengus = Errorengus + 1
                if file == "Resultepo.txt":
                    totalepo = totalepo + 1
                    levenstinedistanceepo.append(ld)
                    weightedlevenshteindepo.append(wld)
                    Phonesepo.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorepo = Errorepo + 1
                if file == "Resultest.txt":
                    totalest = totalest + 1
                    levenstinedistanceest.append(ld)
                    weightedlevenshteindest.append(wld)
                    Phonesest.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorest = Errorest + 1
                if file == "Resulteus.txt":
                    totaleus = totaleus + 1
                    levenstinedistanceeus.append(ld)
                    weightedlevenshteindeus.append(wld)
                    Phoneseus.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroreus = Erroreus + 1
                if file == "Resultfin.txt":
                    totalfin = totalfin + 1
                    levenstinedistancefin.append(ld)
                    weightedlevenshteindfin.append(wld)
                    Phonesfin.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorfin = Errorfin + 1
                if file == "Resultfra-quebec.txt":
                    totalfraquebec = totalfraquebec + 1
                    levenstinedistancefraquebec.append(ld)
                    weightedlevenshteindfraquebec.append(wld)
                    Phonesfraquebec.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorfraquebec = Errorfraquebec + 1
                if file == "Resultgrn.txt":
                    totalgrn = totalgrn + 1
                    levenstinedistancegrn.append(ld)
                    weightedlevenshteindgrn.append(wld)
                    Phonesgrn.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorgrn = Errorgrn + 1
                if file == "Resultina.txt":
                    totalina = totalina + 1
                    levenstinedistanceina.append(ld)
                    weightedlevenshteindina.append(wld)
                    Phonesina.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorina = Errorina + 1
                if file == "Resultind.txt":
                    totalind = totalind + 1
                    levenstinedistanceind.append(ld)
                    weightedlevenshteindind.append(wld)
                    Phonesind.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorind = Errorind + 1
                if file == "Resultjam.txt":
                    totaljam = totaljam + 1
                    levenstinedistancejam.append(ld)
                    weightedlevenshteindjam.append(wld)
                    Phonesjam.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorjam = Errorjam + 1
                if file == "Resultltz-lu.txt":
                    totalitzlu = totalitzlu + 1
                    levenstinedistanceitzlu.append(ld)
                    weightedlevenshteinditzlu.append(wld)
                    Phonesitzlu.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroritzlu = Erroritzlu + 1
                if file == "Resultmlt.txt":
                    totalmlt = totalmlt + 1
                    levenstinedistancemlt.append(ld)
                    weightedlevenshteindmlt.append(wld)
                    Phonesmlt.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errormlt = Errormlt + 1
                if file == "Resultmri.txt":
                    totalmri = totalmri + 1
                    levenstinedistancemri.append(ld)
                    weightedlevenshteindmri.append(wld)
                    Phonesmri.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errormri = Errormri + 1
                if file == "Resultnob.txt":
                    totalnob = totalnob + 1
                    levenstinedistancenob.append(ld)
                    weightedlevenshteindnob.append(wld)
                    Phonesnob.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errornob = Errornob + 1
                if file == "Resultorm.txt":
                    totalorm = totalorm + 1
                    levenstinedistanceorm.append(ld)
                    weightedlevenshteindorm.append(wld)
                    Phonesorm.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errororm = Errororm + 1
                if file == "Resultpap.txt":
                    totalpap = totalpap + 1
                    levenstinedistancepap.append(ld)
                    weightedlevenshteindpap.append(wld)
                    Phonespap.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorpap = Errorpap + 1
                if file == "Resultque.txt":
                    totalque = totalque + 1
                    levenstinedistanceque.append(ld)
                    weightedlevenshteindque.append(wld)
                    Phonesque.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorque = Errorque + 1
                if file == "Resultslk.txt":
                    totalslk = totalslk + 1
                    levenstinedistanceslk.append(ld)
                    weightedlevenshteindslk.append(wld)
                    Phonesslk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorslk = Errorslk + 1
                if file == "Resultspa.txt":
                    totalspa = totalspa + 1
                    levenstinedistancespa.append(ld)
                    weightedlevenshteindspa.append(wld)
                    Phonesspa.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorspa = Errorspa + 1
                if file == "Resultspa-mexico.txt":
                    totalspamexico = totalspamexico + 1
                    levenstinedistancespamexico.append(ld)
                    weightedlevenshteindspamexico.append(wld)
                    Phonesspamexico.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorspamexico = Errorspamexico + 1
                if file == "Resultsqi.txt":
                    totalsqi = totalsqi + 1
                    levenstinedistancesqi.append(ld)
                    weightedlevenshteindsqi.append(wld)
                    Phonessqi.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorsqi = Errorsqi + 1
                if file == "Resultswa.txt":
                    totalswa = totalswa + 1
                    levenstinedistanceswa.append(ld)
                    weightedlevenshteindswa.append(wld)
                    Phonesswa.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorswa = Errorswa + 1
                if file == "Resulttuk.txt":
                    totaltuk = totaltuk + 1
                    levenstinedistancetuk.append(ld)
                    weightedlevenshteindtuk.append(wld)
                    Phonestuk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errortuk = Errortuk + 1
                if file == "Resulttur.txt":
                    totaltur = totaltur + 1
                    levenstinedistancetur.append(ld)
                    weightedlevenshteindtur.append(wld)
                    Phonestur.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errortur = Errortur + 1
                if file == "Resultuzb.txt":
                    totaluzb = totaluzb + 1
                    levenstinedistanceuzb.append(ld)
                    weightedlevenshteinduzb.append(wld)
                    Phonesuzb.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroruzb = Erroruzb + 1
                if file == "Resultvie-c.txt":
                    totalviec = totalviec + 1
                    levenstinedistanceviec.append(ld)
                    weightedlevenshteindviec.append(wld)
                    Phonesviec.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorviec = Errorviec + 1
                if file == "Resultvie-n.txt":
                    totalvien = totalvien + 1
                    levenstinedistancevien.append(ld)
                    weightedlevenshteindvien.append(wld)
                    Phonesvien.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorvien = Errorvien + 1
                if file == "Resultvie-s.txt":
                    totalvies = totalvies + 1
                    levenstinedistancevies.append(ld)
                    weightedlevenshteindvies.append(wld)
                    Phonesvies.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorvies = Errorvies + 1
                if file != "Resultest.txt" and file != "Resultafr.txt" and file != "Resultarg.txt" and file != "Resultaze.txt" and file != "Resultbos.txt" and file != "Resulteng-uk.txt" and file != "Resulteng-us.txt" and file != "Resultepo.txt" and file != "Resulteus.txt" and file != "Resultfin.txt" and file != "Resultfra-quebec.txt" and file != "Resultgrn.txt" and file != "Resultina.txt" and file != "Resultind.txt" and file != "Resultjam.txt" and file != "Resultltz-lu.txt" and file != "Resultmlt.txt" and file != "Resultmri.txt" and file != "Resultnob.txt" and file != "Resultorm.txt" and file != "Resultpap.txt" and file != "Resultque.txt" and file != "Resultslk.txt" and file != "Resultspa.txt" and file != "Resultspa-mexico.txt" and file != "Resultsqi.txt" and file != "Resultswa.txt" and file != "Resulttuk.txt" and file != "Resulttur.txt" and file != "Resultuzb.txt" and file != "Resultvie-c.txt" and file != "Resultvie-n.txt" and file != "Resultvie-s.txt":
                    totalunk = totalunk + 1
                    levenstinedistanceunk.append(ld)
                    weightedlevenshteindunk.append(wld)
                    Phonesunk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorunk = Errorunk + 1
                #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#All data skrivs ut.
#-------------------------------------
confusin = Counter(wrongslist)
print(confusin)
counter = 0
for nume in confusin:
    counter = confusin[nume] + counter
print(counter)
WER = Error/total

print("-------------------------------------------------------------------------------------------------------")
print("All")
print(total)
print(WER)
print(sum(levenstinedistance)/sum(Phones))
print(sum(weightedlevenshteind)/sum(Phones))
print((sum(levenstinedistance)/sum(Phones))-(sum(weightedlevenshteind)/sum(Phones)))
print("-------------------------------------------------------------------------------------------------------")
print("Afrikaans")
print(totalafr)
print(Errorafr/totalafr)
print(sum(levenstinedistanceafr)/sum(Phonesafr))
print(sum(weightedlevenshteindafr)/sum(Phonesafr))
print((sum(levenstinedistanceafr)/sum(Phonesafr))-(sum(weightedlevenshteindafr)/sum(Phonesafr)))
print("-------------------------------------------------------------------------------------------------------")
print("Aragonese")
print(totalarg)
print(Errorarg/totalarg)
print(sum(levenstinedistancearg)/sum(Phonesarg))
print(sum(weightedlevenshteindarg)/sum(Phonesarg))
print((sum(levenstinedistancearg)/sum(Phonesarg))-(sum(weightedlevenshteindarg)/sum(Phonesarg)))
print("-------------------------------------------------------------------------------------------------------")
print("Azerbaijani")
print(totalaze)
print(Erroraze/totalaze)
print(sum(levenstinedistanceaze)/sum(Phonesaze))
print(sum(weightedlevenshteindaze)/sum(Phonesaze))
print((sum(levenstinedistanceaze)/sum(Phonesaze))-(sum(weightedlevenshteindaze)/sum(Phonesaze)))
print("-------------------------------------------------------------------------------------------------------")
print("Bosnian")
print(totalbos)
print(Errorbos/totalbos)
print(sum(levenstinedistancebos)/sum(Phonesbos))
print(sum(weightedlevenshteindbos)/sum(Phonesbos))
print((sum(levenstinedistancebos)/sum(Phonesbos))-(sum(weightedlevenshteindbos)/sum(Phonesbos)))
print("-------------------------------------------------------------------------------------------------------")
print("English UK")
print(totalenguk)
print(Errorenguk/totalenguk)
print(sum(levenstinedistanceenguk)/sum(Phonesenguk))
print(sum(weightedlevenshteindenguk)/sum(Phonesenguk))
print((sum(levenstinedistanceenguk)/sum(Phonesenguk))-(sum(weightedlevenshteindenguk)/sum(Phonesenguk)))
print("-------------------------------------------------------------------------------------------------------")
print("English USA")
print(totalengus)
print(Errorengus/totalengus)
print(sum(levenstinedistanceengus)/sum(Phonesengus))
print(sum(weightedlevenshteindengus)/sum(Phonesengus))
print((sum(levenstinedistanceengus)/sum(Phonesengus))-(sum(weightedlevenshteindengus)/sum(Phonesengus)))
print("-------------------------------------------------------------------------------------------------------")
print("Esperanto")
print(totalepo)
print(Errorepo/totalepo)
print(sum(levenstinedistanceepo)/sum(Phonesepo))
print(sum(weightedlevenshteindepo)/sum(Phonesepo))
print((sum(levenstinedistanceepo)/sum(Phonesepo))-(sum(weightedlevenshteindepo)/sum(Phonesepo)))
print("-------------------------------------------------------------------------------------------------------")
print("Estonian")
print(totalest)
print(Errorest/totalest)
print(sum(levenstinedistanceest)/sum(Phonesest))
print(sum(weightedlevenshteindest)/sum(Phonesest))
print((sum(levenstinedistanceest)/sum(Phonesest))-(sum(weightedlevenshteindest)/sum(Phonesest)))
print("-------------------------------------------------------------------------------------------------------")
print("Basque")
print(totaleus)
print(Erroreus/totaleus)
print(sum(levenstinedistanceeus)/sum(Phoneseus))
print(sum(weightedlevenshteindeus)/sum(Phoneseus))
print((sum(levenstinedistanceeus)/sum(Phoneseus))-(sum(weightedlevenshteindeus)/sum(Phoneseus)))
print("-------------------------------------------------------------------------------------------------------")
print("Finnish")
print(totalfin)
print(Errorfin/totalfin)
print(sum(levenstinedistancefin)/sum(Phonesfin))
print(sum(weightedlevenshteindfin)/sum(Phonesfin))
print((sum(levenstinedistancefin)/sum(Phonesfin))-(sum(weightedlevenshteindfin)/sum(Phonesfin)))
print("-------------------------------------------------------------------------------------------------------")
print("French Quebec")
print(totalfraquebec)
print(Errorfraquebec/totalfraquebec)
print(sum(levenstinedistancefraquebec)/sum(Phonesfraquebec))
print(sum(weightedlevenshteindfraquebec)/sum(Phonesfraquebec))
print((sum(levenstinedistancefraquebec)/sum(Phonesfraquebec))-(sum(weightedlevenshteindfraquebec)/sum(Phonesfraquebec)))
print("-------------------------------------------------------------------------------------------------------")
print("Guarani")
print(totalgrn)
print(Errorgrn/totalgrn)
print(sum(levenstinedistancegrn)/sum(Phonesgrn))
print(sum(weightedlevenshteindgrn)/sum(Phonesgrn))
print((sum(levenstinedistancegrn)/sum(Phonesgrn))-(sum(weightedlevenshteindgrn)/sum(Phonesgrn)))
print("-------------------------------------------------------------------------------------------------------")
print("Interlingua")
print(totalina)
print(Errorina/totalina)
print(sum(levenstinedistanceina)/sum(Phonesina))
print(sum(weightedlevenshteindina)/sum(Phonesina))
print((sum(levenstinedistanceina)/sum(Phonesina))-(sum(weightedlevenshteindina)/sum(Phonesina)))
print("-------------------------------------------------------------------------------------------------------")
print("Indonesian")
print(totalind)
print(Errorind/totalind)
print(sum(levenstinedistanceind)/sum(Phonesind))
print(sum(weightedlevenshteindind)/sum(Phonesind))
print((sum(levenstinedistanceind)/sum(Phonesind))-(sum(weightedlevenshteindind)/sum(Phonesind)))
print("-------------------------------------------------------------------------------------------------------")
print("Jamaican Patois")
print(totaljam)
print(Errorjam/totaljam)
print(sum(levenstinedistancejam)/sum(Phonesjam))
print(sum(weightedlevenshteindjam)/sum(Phonesjam))
print((sum(levenstinedistancejam)/sum(Phonesjam))-(sum(weightedlevenshteindjam)/sum(Phonesjam)))
print("-------------------------------------------------------------------------------------------------------")
print("Itza Lu?")
print(totalitzlu)
print(Erroritzlu/totalitzlu)
print(sum(levenstinedistanceitzlu)/sum(Phonesitzlu))
print(sum(weightedlevenshteinditzlu)/sum(Phonesitzlu))
print((sum(levenstinedistanceitzlu)/sum(Phonesitzlu))-(sum(weightedlevenshteinditzlu)/sum(Phonesitzlu)))
print("-------------------------------------------------------------------------------------------------------")
print("Maltese")
print(totalmlt)
print(Errormlt/totalmlt)
print(sum(levenstinedistancemlt)/sum(Phonesmlt))
print(sum(weightedlevenshteindmlt)/sum(Phonesmlt))
print((sum(levenstinedistancemlt)/sum(Phonesmlt))-(sum(weightedlevenshteindmlt)/sum(Phonesmlt)))
print("-------------------------------------------------------------------------------------------------------")
print("Maori")
print(totalmri)
print(Errormri/totalmri)
print(sum(levenstinedistancemri)/sum(Phonesmri))
print(sum(weightedlevenshteindmri)/sum(Phonesmri))
print((sum(levenstinedistancemri)/sum(Phonesmri))-(sum(weightedlevenshteindmri)/sum(Phonesmri)))
print("-------------------------------------------------------------------------------------------------------")
print("Bockmål")
print(totalnob)
print(Errornob/totalnob)
print(sum(levenstinedistancenob)/sum(Phonesnob))
print(sum(weightedlevenshteindnob)/sum(Phonesnob))
print((sum(levenstinedistancenob)/sum(Phonesnob))-(sum(weightedlevenshteindnob)/sum(Phonesnob)))
print("-------------------------------------------------------------------------------------------------------")
print("Oromo")
print(totalorm)
print(Errororm/totalorm)
print(sum(levenstinedistanceorm)/sum(Phonesorm))
print(sum(weightedlevenshteindorm)/sum(Phonesorm))
print((sum(levenstinedistanceorm)/sum(Phonesorm))-(sum(weightedlevenshteindorm)/sum(Phonesorm)))
print("-------------------------------------------------------------------------------------------------------")
print("Papiamento")
print(totalpap)
print(Errorpap/totalpap)
print(sum(levenstinedistancepap)/sum(Phonespap))
print(sum(weightedlevenshteindpap)/sum(Phonespap))
print((sum(levenstinedistancepap)/sum(Phonespap))-(sum(weightedlevenshteindpap)/sum(Phonespap)))
print("-------------------------------------------------------------------------------------------------------")
print("Quechua")
print(totalque)
print(Errorque/totalque)
print(sum(levenstinedistanceque)/sum(Phonesque))
print(sum(weightedlevenshteindque)/sum(Phonesque))
print((sum(levenstinedistanceque)/sum(Phonesque))-(sum(weightedlevenshteindque)/sum(Phonesque)))
print("-------------------------------------------------------------------------------------------------------")
print("Slovak")
print(totalslk)
print(Errorslk/totalslk)
print(sum(levenstinedistanceslk)/sum(Phonesslk))
print(sum(weightedlevenshteindslk)/sum(Phonesslk))
print((sum(levenstinedistanceslk)/sum(Phonesslk))-(sum(weightedlevenshteindslk)/sum(Phonesslk)))
print("-------------------------------------------------------------------------------------------------------")
print("Spanish C")
print(totalspa)
print(Errorspa/totalspa)
print(sum(levenstinedistancespa)/sum(Phonesspa))
print(sum(weightedlevenshteindspa)/sum(Phonesspa))
print((sum(levenstinedistancespa)/sum(Phonesspa))-(sum(weightedlevenshteindspa)/sum(Phonesspa)))
print("-------------------------------------------------------------------------------------------------------")
print("Spanish M")
print(totalspamexico)
print(Errorspamexico/totalspamexico)
print(sum(levenstinedistancespamexico)/sum(Phonesspamexico))
print(sum(weightedlevenshteindspamexico)/sum(Phonesspamexico))
print((sum(levenstinedistancespamexico)/sum(Phonesspamexico))-(sum(weightedlevenshteindspamexico)/sum(Phonesspamexico)))
print("-------------------------------------------------------------------------------------------------------")
print("Albanian")
print(totalsqi)
print(Errorsqi/totalsqi)
print(sum(levenstinedistancesqi)/sum(Phonessqi))
print(sum(weightedlevenshteindsqi)/sum(Phonessqi))
print((sum(levenstinedistancesqi)/sum(Phonessqi))-(sum(weightedlevenshteindsqi)/sum(Phonessqi)))
print("-------------------------------------------------------------------------------------------------------")
print("Swahili")
print(totalswa)
print(Errorswa/totalswa)
print(sum(levenstinedistanceswa)/sum(Phonesswa))
print(sum(weightedlevenshteindswa)/sum(Phonesswa))
print((sum(levenstinedistanceswa)/sum(Phonesswa))-(sum(weightedlevenshteindswa)/sum(Phonesswa)))
print("-------------------------------------------------------------------------------------------------------")
print("Turkmen")
print(totaltuk)
print(Errortuk/totaltuk)
print(sum(levenstinedistancetuk)/sum(Phonestuk))
print(sum(weightedlevenshteindtuk)/sum(Phonestuk))
print((sum(levenstinedistancetuk)/sum(Phonestuk))-(sum(weightedlevenshteindtuk)/sum(Phonestuk)))
print("-------------------------------------------------------------------------------------------------------")
print("Turkish")
print(totaltur)
print(Errortur/totaltur)
print(sum(levenstinedistancetur)/sum(Phonestur))
print(sum(weightedlevenshteindtur)/sum(Phonestur))
print((sum(levenstinedistancetur)/sum(Phonestur))-(sum(weightedlevenshteindtur)/sum(Phonestur)))
print("-------------------------------------------------------------------------------------------------------")
print("Uzbek")
print(totaluzb)
if totaluzb != 0:
    print(Erroruzb/totaluzb)
if (sum(Phonesuzb)) != 0:  
    print(sum(levenstinedistanceuzb)/sum(Phonesuzb))
    print(sum(weightedlevenshteinduzb)/sum(Phonesuzb))
    print((sum(levenstinedistanceuzb)/sum(Phonesuzb))-(sum(weightedlevenshteinduzb)/sum(Phonesuzb)))
print("-------------------------------------------------------------------------------------------------------")
print("vietnamese C")
print(totalviec)
if totalviec != 0:
    print(Errorviec/totalviec)
if (sum(Phonesviec)) != 0:  
    print(sum(levenstinedistanceviec)/sum(Phonesviec))
    print(sum(weightedlevenshteindviec)/sum(Phonesviec))
    print((sum(levenstinedistanceviec)/sum(Phonesviec))-(sum(weightedlevenshteindviec)/sum(Phonesviec)))
print("-------------------------------------------------------------------------------------------------------")
print("vietnamese N")
print(totalvien)
if totalvien != 0:
    print(Errorvien/totalvien)
if (sum(Phonesvien)) != 0:  
    print(sum(levenstinedistancevien)/sum(Phonesvien))
    print(sum(weightedlevenshteindvien)/sum(Phonesvien))
    print((sum(levenstinedistancevien)/sum(Phonesvien))-(sum(weightedlevenshteindvien)/sum(Phonesvien)))
print("-------------------------------------------------------------------------------------------------------")
print("vietnamese S")
print(totalvies)
if totalvies != 0:
    print(Errorvies/totalvies)
if (sum(Phonesvies)) != 0:  
    print(sum(levenstinedistancevies)/sum(Phonesvies))
    print(sum(weightedlevenshteindvies)/sum(Phonesvies))
    print((sum(levenstinedistancevies)/sum(Phonesvies))-(sum(weightedlevenshteindvies)/sum(Phonesvies)))
print("-------------------------------------------------------------------------------------------------------")
print("Unknow language")
print(totalunk)
if totalunk != 0:
    print(Errorunk/totalunk)
if (sum(Phonesunk)) != 0:  
    print(sum(levenstinedistanceunk)/sum(Phonesunk))
    print(sum(weightedlevenshteindunk)/sum(Phonesunk))
    print((sum(levenstinedistanceunk)/sum(Phonesunk))-(sum(weightedlevenshteindunk)/sum(Phonesunk)))
print("-------------------------------------------------------------------------------------------------------")
print((total)-(totalafr + totalarg + totalaze + totalbos + totalenguk + totalengus + totalepo + totalest + totaleus + totalfin + totalfraquebec + totalgrn + totalina + totalind + totaljam + totalitzlu + totalmlt + totalmri + totalnob + totalorm + totalpap + totalque + totalslk + totalspa + totalspamexico + totalsqi + totalswa + totaltuk + totaltur + totaluzb + totalviec + totalvien + totalvies + totalunk))
#---------------------------------------------------------------------------------------------------------------------