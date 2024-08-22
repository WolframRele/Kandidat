#för kodförklaring, kolla motsvarande fil i phonetisaurus. enda skillnaden mellan filerna är att denna har lite enklare datainhämtning.
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
WightAvriger = 4.24126389646
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
insert_costs = np.ones(128, dtype=np.float64)
delete_costs = np.ones(128, dtype=np.float64)
substitute_costs = np.ones((128, 128), dtype=np.float64)
substitute_costs2 = np.ones((128, 128), dtype=np.float64)  
Distance = open("TruDistance.txt", "r", encoding= "utf-8")
for line in Distance:
    caracters,vector = line.split("	")
    A,B = caracters.split(",")
    substitute_costs2[ord(A), ord(B)] = (float(vector)/WightAvriger)
    substitute_costs2[ord(B), ord(A)] = (float(vector)/WightAvriger)
Gesses = ("DEEPreultafr.txt","DEEPreultarg.txt","DEEPreultaze.txt","DEEPreultbos.txt","DEEPreulteng-uk.txt","DEEPreulteng-us.txt","DEEPreultepo.txt","DEEPreulteus.txt","DEEPreultfin.txt","DEEPreultfra-quebec.txt","DEEPreultgrn.txt","DEEPreultina.txt","DEEPreultind.txt","DEEPreultjam.txt","DEEPreultltz-lu.txt","DEEPreultmlt.txt","DEEPreultmri.txt","DEEPreultnob.txt","DEEPreultorm.txt","DEEPreultpap.txt","DEEPreultque.txt","DEEPreultslk.txt","DEEPreultspa.txt","DEEPreultspa-mexico.txt","DEEPreultsqi.txt","DEEPreultswa.txt","DEEPreulttuk.txt","DEEPreulttur.txt","DEEPreultvie-c.txt","DEEPreultvie-n.txt","DEEPreultvie-s.txt")
for file in Gesses:
    Results = open(file, "r", encoding= "utf-8")
    ResultL = []
    word = ""
    guideL = {}
    test = int()
    for line in Results:
        Words = line.split(" ")
        ResultL.append((Words[0],Words[1]))
    Results.close
    Word = ""
    if file == "DEEPreultafr.txt":
       guide = open("guidewfafr.txt", "r", encoding= "utf-8")
    elif file == "DEEPreultarg.txt":
        guide = open("guidewfarg.txt", "r", encoding= "utf-8")
    elif file == "DEEPreultaze.txt":
        guide = open("guidewfaze.txt", "r", encoding= "utf-8")
    elif file == "DEEPreultbos.txt":
        guide = open("guidewfbos.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreulteng-uk.txt":
        guide = open("guidewfeng-uk.txt", "r", encoding= "utf-8")
    elif file == "DEEPreulteng-us.txt":
        guide = open("guidewfeng-us.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultepo.txt":
        guide = open("guidewfepo.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultest.txt":
        guide = open("guidewfest.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreulteus.txt":
        guide = open("guidewfeus.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultfin.txt":
        guide = open("guidewffin.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultfra-quebec.txt":
        guide = open("guidewffra-quebec.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultgrn.txt":
        guide = open("guidewfgrn.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultina.txt":
        guide = open("guidewfina.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultind.txt":
        guide = open("guidewfind.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultjam.txt":
        guide = open("guidewfjam.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultltz-lu.txt":
        guide = open("guidewfltz-lu.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultmlt.txt":
        guide = open("guidewfmlt.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultmri.txt":
        guide = open("guidewfmri.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultnob.txt":
        guide = open("guidewfnob.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultorm.txt":
        guide = open("guidewform.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultpap.txt":
        guide = open("guidewfpap.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultque.txt":
        guide = open("guidewfque.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultslk.txt":
        guide = open("guidewfslk.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultspa.txt":
        guide = open("guidewfspa.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultspa-mexico.txt":
        guide = open("guidewfspa-mexico.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultsqi.txt":
        guide = open("guidewfsqi.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultswa.txt":
        guide = open("guidewfswa.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreulttuk.txt":
        guide = open("guidewftuk.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreulttur.txt":
        guide = open("guidewftur.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultuzb.txt":
        guide = open("guidewfuzb.txt", "r", encoding= "utf-8")
    elif file == "DEEPreultvie-c.txt":
        guide = open("guidewfvie-c.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultvie-n.txt":
        guide = open("guidewfvie-n.txt", "r", encoding= "utf-8") 
    elif file == "DEEPreultvie-s.txt":
        guide = open("guidewfvie-s.txt", "r", encoding= "utf-8")
    else:
        guide = open("guidewf.txt", "r", encoding= "utf-8")
    for i,line in enumerate(guide):
        words = line.split("	")
        guideL[words[0]] = words[1][:-1]
    if len(guideL) == len(ResultL):
        print("True")
    else:
        print("False" + " " +  str(len(guideL)) + " " + str(len(ResultL)))
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
                if file == "DEEPreultafr.txt":
                    totalafr = totalafr + 1
                    levenstinedistanceafr.append(ld)
                    weightedlevenshteindafr.append(wld)
                    Phonesafr.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorafr = Errorafr + 1
                if file == "DEEPreultarg.txt":
                    totalarg = totalarg + 1
                    levenstinedistancearg.append(ld)
                    weightedlevenshteindarg.append(wld)
                    Phonesarg.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorarg = Errorarg + 1
                if file == "DEEPreultaze.txt":
                    totalaze = totalaze + 1
                    levenstinedistanceaze.append(ld)
                    weightedlevenshteindaze.append(wld)
                    Phonesaze.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroraze = Erroraze + 1
                if file == "DEEPreultbos.txt":
                    totalbos = totalbos + 1
                    levenstinedistancebos.append(ld)
                    weightedlevenshteindbos.append(wld)
                    Phonesbos.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorbos = Errorbos + 1
                if file == "DEEPreulteng-uk.txt":
                    totalenguk = totalenguk + 1
                    levenstinedistanceenguk.append(ld)
                    weightedlevenshteindenguk.append(wld)
                    Phonesenguk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorenguk = Errorenguk + 1
                if file == "DEEPreulteng-us.txt":
                    totalengus = totalengus + 1
                    levenstinedistanceengus.append(ld)
                    weightedlevenshteindengus.append(wld)
                    Phonesengus.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorengus = Errorengus + 1
                if file == "DEEPreultepo.txt":
                    totalepo = totalepo + 1
                    levenstinedistanceepo.append(ld)
                    weightedlevenshteindepo.append(wld)
                    Phonesepo.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorepo = Errorepo + 1
                if file == "DEEPreultest.txt":
                    totalest = totalest + 1
                    levenstinedistanceest.append(ld)
                    weightedlevenshteindest.append(wld)
                    Phonesest.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorest = Errorest + 1
                if file == "DEEPreulteus.txt":
                    totaleus = totaleus + 1
                    levenstinedistanceeus.append(ld)
                    weightedlevenshteindeus.append(wld)
                    Phoneseus.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroreus = Erroreus + 1
                if file == "DEEPreultfin.txt":
                    totalfin = totalfin + 1
                    levenstinedistancefin.append(ld)
                    weightedlevenshteindfin.append(wld)
                    Phonesfin.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorfin = Errorfin + 1
                if file == "DEEPreultfra-quebec.txt":
                    totalfraquebec = totalfraquebec + 1
                    levenstinedistancefraquebec.append(ld)
                    weightedlevenshteindfraquebec.append(wld)
                    Phonesfraquebec.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorfraquebec = Errorfraquebec + 1
                if file == "DEEPreultgrn.txt":
                    totalgrn = totalgrn + 1
                    levenstinedistancegrn.append(ld)
                    weightedlevenshteindgrn.append(wld)
                    Phonesgrn.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorgrn = Errorgrn + 1
                if file == "DEEPreultina.txt":
                    totalina = totalina + 1
                    levenstinedistanceina.append(ld)
                    weightedlevenshteindina.append(wld)
                    Phonesina.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorina = Errorina + 1
                if file == "DEEPreultind.txt":
                    totalind = totalind + 1
                    levenstinedistanceind.append(ld)
                    weightedlevenshteindind.append(wld)
                    Phonesind.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorind = Errorind + 1
                if file == "DEEPreultjam.txt":
                    totaljam = totaljam + 1
                    levenstinedistancejam.append(ld)
                    weightedlevenshteindjam.append(wld)
                    Phonesjam.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorjam = Errorjam + 1
                if file == "DEEPreultltz-lu.txt":
                    totalitzlu = totalitzlu + 1
                    levenstinedistanceitzlu.append(ld)
                    weightedlevenshteinditzlu.append(wld)
                    Phonesitzlu.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroritzlu = Erroritzlu + 1
                if file == "DEEPreultmlt.txt":
                    totalmlt = totalmlt + 1
                    levenstinedistancemlt.append(ld)
                    weightedlevenshteindmlt.append(wld)
                    Phonesmlt.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errormlt = Errormlt + 1
                if file == "DEEPreultmri.txt":
                    totalmri = totalmri + 1
                    levenstinedistancemri.append(ld)
                    weightedlevenshteindmri.append(wld)
                    Phonesmri.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errormri = Errormri + 1
                if file == "DEEPreultnob.txt":
                    totalnob = totalnob + 1
                    levenstinedistancenob.append(ld)
                    weightedlevenshteindnob.append(wld)
                    Phonesnob.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errornob = Errornob + 1
                if file == "DEEPreultorm.txt":
                    totalorm = totalorm + 1
                    levenstinedistanceorm.append(ld)
                    weightedlevenshteindorm.append(wld)
                    Phonesorm.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errororm = Errororm + 1
                if file == "DEEPreultpap.txt":
                    totalpap = totalpap + 1
                    levenstinedistancepap.append(ld)
                    weightedlevenshteindpap.append(wld)
                    Phonespap.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorpap = Errorpap + 1
                if file == "DEEPreultque.txt":
                    totalque = totalque + 1
                    levenstinedistanceque.append(ld)
                    weightedlevenshteindque.append(wld)
                    Phonesque.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorque = Errorque + 1
                if file == "DEEPreultslk.txt":
                    totalslk = totalslk + 1
                    levenstinedistanceslk.append(ld)
                    weightedlevenshteindslk.append(wld)
                    Phonesslk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorslk = Errorslk + 1
                if file == "DEEPreultspa.txt":
                    totalspa = totalspa + 1
                    levenstinedistancespa.append(ld)
                    weightedlevenshteindspa.append(wld)
                    Phonesspa.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorspa = Errorspa + 1
                if file == "DEEPreultspa-mexico.txt":
                    totalspamexico = totalspamexico + 1
                    levenstinedistancespamexico.append(ld)
                    weightedlevenshteindspamexico.append(wld)
                    Phonesspamexico.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorspamexico = Errorspamexico + 1
                if file == "DEEPreultsqi.txt":
                    totalsqi = totalsqi + 1
                    levenstinedistancesqi.append(ld)
                    weightedlevenshteindsqi.append(wld)
                    Phonessqi.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorsqi = Errorsqi + 1
                if file == "DEEPreultswa.txt":
                    totalswa = totalswa + 1
                    levenstinedistanceswa.append(ld)
                    weightedlevenshteindswa.append(wld)
                    Phonesswa.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorswa = Errorswa + 1
                if file == "DEEPreulttuk.txt":
                    totaltuk = totaltuk + 1
                    levenstinedistancetuk.append(ld)
                    weightedlevenshteindtuk.append(wld)
                    Phonestuk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errortuk = Errortuk + 1
                if file == "DEEPreulttur.txt":
                    totaltur = totaltur + 1
                    levenstinedistancetur.append(ld)
                    weightedlevenshteindtur.append(wld)
                    Phonestur.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errortur = Errortur + 1
                if file == "DEEPreultuzb.txt":
                    totaluzb = totaluzb + 1
                    levenstinedistanceuzb.append(ld)
                    weightedlevenshteinduzb.append(wld)
                    Phonesuzb.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Erroruzb = Erroruzb + 1
                if file == "DEEPreultvie-c.txt":
                    totalviec = totalviec + 1
                    levenstinedistanceviec.append(ld)
                    weightedlevenshteindviec.append(wld)
                    Phonesviec.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorviec = Errorviec + 1
                if file == "DEEPreultvie-n.txt":
                    totalvien = totalvien + 1
                    levenstinedistancevien.append(ld)
                    weightedlevenshteindvien.append(wld)
                    Phonesvien.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorvien = Errorvien + 1
                if file == "DEEPreultvie-s.txt":
                    totalvies = totalvies + 1
                    levenstinedistancevies.append(ld)
                    weightedlevenshteindvies.append(wld)
                    Phonesvies.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorvies = Errorvies + 1
                if file != "DEEPreultest.txt" and file != "DEEPreultafr.txt" and file != "DEEPreultarg.txt" and file != "DEEPreultaze.txt" and file != "DEEPreultbos.txt" and file != "DEEPreulteng-uk.txt" and file != "DEEPreulteng-us.txt" and file != "DEEPreultepo.txt" and file != "DEEPreulteus.txt" and file != "DEEPreultfin.txt" and file != "DEEPreultfra-quebec.txt" and file != "DEEPreultgrn.txt" and file != "DEEPreultina.txt" and file != "DEEPreultind.txt" and file != "DEEPreultjam.txt" and file != "DEEPreultltz-lu.txt" and file != "DEEPreultmlt.txt" and file != "DEEPreultmri.txt" and file != "DEEPreultnob.txt" and file != "DEEPreultorm.txt" and file != "DEEPreultpap.txt" and file != "DEEPreultque.txt" and file != "DEEPreultslk.txt" and file != "DEEPreultspa.txt" and file != "DEEPreultspa-mexico.txt" and file != "DEEPreultsqi.txt" and file != "DEEPreultswa.txt" and file != "DEEPreulttuk.txt" and file != "DEEPreulttur.txt" and file != "DEEPreultuzb.txt" and file != "DEEPreultvie-c.txt" and file != "DEEPreultvie-n.txt" and file != "DEEPreultvie-s.txt":
                    totalunk = totalunk + 1
                    levenstinedistanceunk.append(ld)
                    weightedlevenshteindunk.append(wld)
                    Phonesunk.append(p)
                    if gese[1].replace(" ","") != guideL[gese[0]].replace(" ",""):
                        Errorunk = Errorunk + 1
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
