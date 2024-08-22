#Detta program förbereder data genom att formatera den så att den går att testa på. filen tar också fram ett facit register för testdatan.
from asjp import ipa2asjp, asjp2ipa, tokenise
asjpL = []
wordL = []
info = 0
#Här väljer man datan man vill testa på.
Files = ("vie-s.tsv")
curentfile = open(Files, "r", encoding = "utf-8")
for line in curentfile:
	Sline = line.split("	")
	#Ordet hoppas över om någon av dessa karaktärer finns i den ortografiska formen då DEEPphonemizer fick problem med dom.
	if "(" in Sline[1][:-1] or "ʼ" in Sline[1][:-1] or "T" in Sline[1][:-1] or "X" in Sline[1][:-1] or "Φ" in Sline[1][:-1] or "'" in Sline[1][:-1] or "A" in Sline[1][:-1] or "B" in Sline[1][:-1] or "C" in Sline[1][:-1] or "D" in Sline[1][:-1] or "E" in Sline[1][:-1] or "F" in Sline[1][:-1] or "G" in Sline[1][:-1] or "H" in Sline[1][:-1] or "I" in Sline[1][:-1] or "J" in Sline[1][:-1] or "K" in Sline[1][:-1] or "L" in Sline[1][:-1] or "M" in Sline[1][:-1] or "ᵐ" in Sline[1][:-1] or "N" in Sline[1][:-1] or "ᵑ" in Sline[1][:-1] or "O" in Sline[1][:-1] or "P" in Sline[1][:-1] or "R" in Sline[1][:-1] or "S" in Sline[1][:-1] or "U" in Sline[1][:-1] or "V" in Sline[1][:-1] or "W" in Sline[1][:-1] or "Y" in Sline[1][:-1] or "Z" in Sline[1][:-1]:
		1+1
	else:
		#Översätter IPA till ASJP
		asjp = ipa2asjp(Sline[1][:-1])
		asjpL.append(asjp)
		wordL.append(Sline[0])
		info = info + 1
	print(info)
#Skriver datan till önskad plats
#-----------------------------------------------------
data = open("guidevie-s.txt", "a", encoding = "utf-8")
data2 = open("guidewfvie-s.txt", "a", encoding = "utf-8")
for pos,item in enumerate(asjpL):
	data.write(wordL[pos] + "\n")
	data2.write(wordL[pos] + "	" + item + "\n")
#--------------------------------------------------------