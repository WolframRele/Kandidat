#För kodförklaring, kolla Distanser. Denna fill gör samma sak fast för vokaler.
import math
phoneD = {}
distanceD = {}
asjpD = {"i":("i","I","y","Y"),"e":("e","ø"),"E":("a","æ","ɛ","œ","ɶ"),"3":("ɨ","ɘ","ə","ɜ","ʉ","ɵ","ɞ"),"a":("ɐ"),"u":("ɯ","u"),"o":("ɤ","ʌ","ɑ","o","ɔ","ɒ")}
asjpdistanceD = {}
file = open("vovlepos.txt", "r", encoding = "utf-8")
for line in file:
	line=line[:-1]
	phone = line.split("	")
	phoneD[phone[0]] = (float(phone[1]),float(phone[2]),float(phone[3]))
	keylist = list(phoneD.keys())
for key in phoneD:
	for key2 in keylist:
		distance = abs(math.sqrt(pow(phoneD[key][0]-phoneD[key2][0],2) + pow(phoneD[key][1]-phoneD[key2][1],2) + pow(phoneD[key][2]-phoneD[key2][2],2)))
		distanceD[key+","+key2] = distance
	keylist.remove(key)	
for key4 in distanceD:
	keys = key4.split(",")
	dumilist = []
	for key5 in asjpD:
		for key6 in asjpD:
			if type(asjpD[key5]) == tuple:
				for ipa in asjpD[key5]:
					if type(asjpD[key6]) == tuple:
						for ipa2 in asjpD[key6]:
							if keys[0] == ipa and keys[1] == ipa2:
								if (key5 + "," + key6) in list(asjpdistanceD.keys()):
									asjpdistanceD[key5 + "," + key6].append(distanceD[key4])
								elif (key6 + "," + key5) in list(asjpdistanceD.keys()):
									asjpdistanceD[key6 + "," + key5].append(distanceD[key4])
								else:
									dumilist.append(distanceD[key4])
									asjpdistanceD[key5 + "," + key6] = dumilist
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
for key7 in asjpdistanceD:
	Adistance = 0
	for distance2 in asjpdistanceD[key7]:
		Adistance = Adistance + distance2
	asjpdistanceD[key7] = (Adistance/len(asjpdistanceD[key7]))
data = open("distanceVovels.txt", "a", encoding = "utf-8")
for key3 in asjpdistanceD:
	data.write(key3 + "	" + str(asjpdistanceD[key3]) + "\n")
