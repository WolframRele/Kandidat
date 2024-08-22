#Denna fil bygger fonem distanse.
import math
phoneD = {}
distanceD = {}
#Matchning för vilka IPA karaktär som representeras av vilka ASJP karaktärer.
asjpD = {"p":("p","ɸ"),"b":("b","β"),"m":("m"),"f":("f"),"v":("v"),"8":("θ","ð"),"4":("n̪"),"t":("t"),"d":("d"),"s":("s"),"z":("z"),"c":("ts","dz"),"n":("n"),"S":("ʃ"),"Z":("ʒ"),"C":("tʃ"),"j":("dʒ"),"T":("c","ɟ"),"5":("ɲ"),"k":("k"),"g":("g"),"x":("x","ɣ"),"N":("ŋ"),"q":("q"),"G":("G"),"X":("X","ʁ","ħ","ʕ"),"7":("ʔ"),"h":("h","ɦ"),"l":("l"),"L":("L","ɭ","ʎ"),"w":("w"),"y":("j"),"r":("r","ʀ","ɾ","ɽ","ɺ","ɻ"),"!":("ǃ","ǀ","ǁ","ǂ")}
asjpdistanceD = {}
#Här matar man in en list med 4 dimensionella punkter som representerar IPA karaktärer.
file = open("phonepos.txt", "r", encoding = "utf-8")
for line in file:
	line=line[:-1]
	phone = line.split("	")
	phoneD[phone[0]] = (float(phone[1]),float(phone[2]),float(phone[3]),float(phone[4]))
	keylist = list(phoneD.keys())
# Här räknas distansen mellan alla fonem.
# ------------------------------------------------
for key in phoneD:
	for key2 in keylist:
		distance = abs(math.sqrt(pow(phoneD[key][0]-phoneD[key2][0],2) + pow(phoneD[key][1]-phoneD[key2][1],2) + pow(phoneD[key][2]-phoneD[key2][2],2) + pow(phoneD[key][3]-phoneD[key2][3],2)))
		distanceD[key+","+key2] = distance
	keylist.remove(key)
#----------------------------------------------------

#Här matchas IPA distansen med dess ASJP karaktär
#----------------------------------------------------------------	
for key4 in distanceD:
	keys = key4.split(",")
	dumilist = []
	for key5 in asjpD:
		for key6 in asjpD:
			#If satser som denna kollar om ASJP karaktären matchar med 1 eller flera IPA karaktärer
			if type(asjpD[key5]) == tuple:
				for ipa in asjpD[key5]:
					if type(asjpD[key6]) == tuple:
						for ipa2 in asjpD[key6]:
							if keys[0] == ipa and keys[1] == ipa2:
								#kollar så att distansen mellan 2 karaktärer inte redan finns i listan. Om inte adderas den med distansen och om denn finns läggs distansen till.
								#------------------------------------------------------------
								if (key5 + "," + key6) in list(asjpdistanceD.keys()):
									asjpdistanceD[key5 + "," + key6].append(distanceD[key4])
								elif (key6 + "," + key5) in list(asjpdistanceD.keys()):
									asjpdistanceD[key6 + "," + key5].append(distanceD[key4])
								else:
									dumilist.append(distanceD[key4])
									asjpdistanceD[key5 + "," + key6] = dumilist
								#--------------------------------------------------------------
					else:
						if keys[0] == ipa and keys[1] == asjpD[key6]:
							if (key5 + "," + key6) in list(asjpdistanceD.keys()):
								asjpdistanceD[key5 + "," + key6].append(distanceD[key4])
							elif (key6 + "," + key5) in list(asjpdistanceD.keys()):
								asjpdistanceD[key6 + "," + key5].append(distanceD[key4])
							else:
								dumilist.append(distanceD[key4])
								asjpdistanceD[key5 + "," + key6] = dumilist
			else:
				if type(asjpD[key6]) == tuple:
					for ipa2 in asjpD[key6]:
						if keys[0] == asjpD[key5] and keys[1] == ipa2:
							if (key5 + "," + key6) in list(asjpdistanceD.keys()):
								asjpdistanceD[key5 + "," + key6].append(distanceD[key4])
							elif (key6 + "," + key5) in list(asjpdistanceD.keys()):
								asjpdistanceD[key6 + "," + key5].append(distanceD[key4])
							else:
								dumilist.append(distanceD[key4])
								asjpdistanceD[key5 + "," + key6] = dumilist
				else:
					if keys[0] == asjpD[key5] and keys[1] == asjpD[key6]:
						if (key5 + "," + key6) in list(asjpdistanceD.keys()):
							asjpdistanceD[key5 + "," + key6].append(distanceD[key4])
						elif (key6 + "," + key5) in list(asjpdistanceD.keys()):
							asjpdistanceD[key6 + "," + key5].append(distanceD[key4])
						else:
							dumilist.append(distanceD[key4])
							asjpdistanceD[key5 + "," + key6] = dumilist
#------------------------------------------------------------------------------------

#här ges en genomsnittligt distans till alla fonem kombinationer från alla värden dom har.
#---------------------------------------------------------------------------------------
for key7 in asjpdistanceD:
	Adistance = 0
	for distance2 in asjpdistanceD[key7]:
		Adistance = Adistance + distance2
	asjpdistanceD[key7] = (Adistance/len(asjpdistanceD[key7]))
#--------------------------------------------------------------------------------------

#Här skrivs distansen mellan alla fonem till önskad plats.
#-----------------------------------------------------------
data = open("distance.txt", "a", encoding = "utf-8")
for key3 in asjpdistanceD:
	data.write(key3 + "	" + str(asjpdistanceD[key3]) + "\n")
#------------------------------------------------------------
