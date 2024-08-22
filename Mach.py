#Denna fil hittar vilka ASJP ord Som Har motsvarigheter i biblar.
import regex
answerLF = []
ContentLF = []
Maches = []
Result = []
ilist = []
#Data in matning.
#-------------------------
file = open("raw_forms.csv", "r", encoding = "utf-8")
cheker = open("asjp.tab", "r", encoding = "utf-8")
#--------------------------------------------------
# Rad 1 innehåller alla ord på engelska.
answer = cheker.readlines(1)

#Dom 7 första delarna på en rad är språkdata och inte ord.
answerL = str(answer).split(str(answer)[7])

#Tar bort rester får filformatet som inte ska vara med.
for catergory in answerL[:-1]:
	if catergory[0] == "t" or catergory[0] == "[":
		answerLF.append(catergory[1:])
	else:
		answerLF.append(catergory)

# Hämtar och rensar data för data filen.
content=file.readlines(1)
contentL = str(content).split(",")
for contentK in contentL:
		if contentK[0] == "t" or contentK[0] == "[":
			ContentLF.append(contentK[1:])
		else:
			ContentLF.append(contentK)

#Hittar matchningar med dom engelska orden i datafilen.
for pos, catergoryLF  in enumerate(answerLF):
	if catergoryLF in ContentLF:
		Maches.append((catergoryLF,pos))
print(Maches)
#Här hämtas den data som matchar från datafilen.
for line in file:
	lineS = str(line).split(",")
	for Name,pos in Maches:
		for position,Ewords in enumerate(ContentLF):
			if Ewords == Name:
				LineSL =  regex.sub(r'[^\p{Latin}]', u'', lineS[position])
				if lineS[position] != "":
					Result.append((lineS[0][:3],Name,lineS[position],pos))


#Sparar matchningarna på önskad plats.
data = open("words.txt", "a", encoding = "utf-8")
for i,line in enumerate(cheker):
	if i == 0:
		t_b = line[3]
	lineSP = line.split(t_b)
	for lang,wordE,wordL,pos2 in Result:
		if lang in lineSP[9]:
			if lineSP[pos2] != "":
				#Hoppar dessa karaktärer då dom inte är latinska.
				if "," not in lineSP[pos2] and " " not in lineSP[pos2] and not any(caracter in wordL for caracter in ["า","н","ы","о","а","เ","б","з","е","น","д","к","ห","т","р","в","г","ร","م","ا","ฟ","ч","ป","ว","ن","ด","і","μ","ื","ा","ล","л","и","ิ","у","ไ","м","с","َ","া","ل","α","υ","ι","ค","ต","س","τ","ρ","ر","ም","โ","ц","ت","ย","х","्","ู","و","ง","்","ه","र","ν","እ","ข","ภ","်","ج","ሳ","ъ","त","ह","র","າ","ေ","ب","ደ","ን","ເ","ก","్","ж","گ","ο","د","က","ی","χ","ብ","ວ","း","క","п","ग","ल","म","์","໌","ါ","င","อ","й","ӕ","ش","আ","θ","ܘ","ዋ","ዓ","ከ","្","ม","ຢ","บ","ర","ш","ु","ड","न","π","ນ","ດ","ົ","ல","త","ү","щ","خ","ङ","প","ম","κ","ລ","ك","တ","پ","ά","ີ","ຫ","ມ","ບ","ာ","่","த","ர","ப","қ","ف","آ","ि","े","प","ܟ","ܢ","ح","ራ","ት","መ","໊","க","ो","आ","स","क","হ","ন","থ","্","ক","ْ","ܐ","ّ","យ","ງ","ຍ","ປ","ီ","့","ம","న","ӱ","ھ","ہ","ਰ","ਾ","ί","ψ","ա","կ","ይ","ለ","ዊ","ሓ","ኒ","ኽ","ܠ","ክ","ሣ","ⲟ","ⲥ","ተ","ↄ","ា","ម","ອ","ື","ຮ","ၤ","ပ","မ","ွ","သ","ိ","้","ந","ை","வ","ள","ெ","һ","ख","़","द","छ","ं","়","ড","ু","গ","ত","ছ","ύ","ω","φ","ε","ܪ","ُ","ሊ","ሌ","ል","አ","ር","ማ","ភ","ង","ើ","ກ","ฑ","ຕ","ໂ","ສ","ျ","ယ","ြ","အ","ု","ี","ः","இ","ற","ன","మ","ు","밤","흰","름","구","별","피","자","여","리","우","ю","ё","ک","چ","ੱ","ਪ","ਤ","ର","୍","ब","थ","σ","η","ի","ր","ւ","ե","כ","ו","ረ","ዀ","ܒ","ጋ","ድ","ኑ","ក","ថ","ី","រ","ន","់","ຟ","ໄ","ພ","ฮ","๊","ะ","ະ","ဲ","ှ","ฺ","แ","ি","எ","ె","ం","ల","พ","ష","ර","ා","්","ప","ే","산","지","ې","ى","ӑ","ز","ତ","फ","ी","λ","ܝ","ܛ","ָ","ּ","ה","ל","א","י","ي","ܲ","ʿ","ጉ","ሹ","ⲩ","ⲓ","ϥ","ⲛ","ላ","ዶ","ጃ","ሻ","ግ","ዣ","ቢ","ሃ","","ዉ","ប","ំ","ល","ព","ផ","ឈ","ត","ស","ຄ","້","ဆ","ဉ","ည","ท","ซ","ল","য়","ও","ॽ","य","ா","ு","ே","ி","ச","ட","ீ","ண","ಿ","ಷ","್","ಕ","ಪ","ా","డ","ొ","చ","ట","స","ిื","ీ","ь","ۇ","ق","җ","ұ","ҙ","ҳ","غ","ئ","ێ","ڑ","ක","ත","න","ੜ","ਹ","ਗ","ਅ","ਥ","ੇ","ି","ପ","ା","ମ","ढ","भ","व","श","έ","ἵ","ἰ","ἡ","շ","գ","ղ","տ","ս","ն","ո","ֶ","ձ","ש","ב","ג","ד","נ","ቶ","ቈ","݂","ܵ","ܡ","ܸ","ܕ","ܼ","ܚ","ጭ","ነ","ና","ች","ፎ","ወ","ሴ","ሉ","ሁ","ጾ","ጽ","ሱ","ሞ","ሮ","ፕ","ኖ","ዱ","ዜ","ቤ","ሜ","ጡ","ቁ","ኳ","ጎ","ํ","ุ","ช","็","អ","ិ","ູ","ဴ","လ","ব","ং","স","চ","इ","ಳ","ಗ","ఘ","అ","ద","ఉ","я","ф","니","아","들","새","ә","ە","ғ","ҫ","ө","ҡ","ј","ћ","ѕ","ӯ","ू","ි","ද","ේ","ල","ු","ස","ම","ප","අ","ବ","ନ","ଗ","ଅ","ଥ","କ","ଛ","ଭ","ଆ","ँ","ै","अ","િ","ન","્","ગ","ી","લ","છ","ા","મ","ણ","પ","આ","ἷ","ὄ","ռ","լ","մ","ِ","ְ","ר","ׁ","ֵ","ן","ֹ","ם","ٱ","ܹ","ኮ","ዹ","ሚ","ታ","ኦ","ዦ","ሎ","ቀ","በ","ቃ","ዙ","ቻ","ቴ","ፆ","ꬃ","ህ","ኬ","ሀ","ዲ","ኩ","ሙ","ጊ"]):
					#Splittar fonemen då Phonetisaurus behöver det.
					#----------------------------------------------------
					spliter = lineSP[pos2]
					Ospliter = spliter
					spliter_length = len(spliter)
					for pos3,i in enumerate(spliter):
						if spliter_length-1 < pos3 + 2:
							blocker1 = 2
						else:
							blocker1 = 0
						if spliter_length-1 < pos3 + 1:
							blocker2 = 1
						else:
							blocker2 = 0
						if spliter_length-1 < pos3 + 3:
							blocker3 = 3
						else:
							blocker3 = 0
						print( str(spliter_length) + " " + spliter + " " + str(pos3) + " " + str(blocker2)+spliter[pos3+1-blocker2]+ " " + str(blocker1)+spliter[pos3+2-blocker1])
						if i != "~" and Ospliter[pos3+1-blocker2] != "~" and Ospliter[pos3+2-blocker1] != "~" and i != "$" and Ospliter[pos3+1-blocker2] != "$" and Ospliter[pos3+2-blocker1] != "$" and Ospliter[pos3+3-blocker3] != "$" and i not in ilist and i != "*" and Ospliter[pos3+1-blocker2] != "*" and pos3 != spliter_length-1:
							spliter=spliter.replace(i, i + " ")
						elif i == "~" or i == "$" or i == "*" and i not in ilist:
							spliter=spliter.replace(i, i + " ")
						ilist.append(i)
						if len(ilist) == spliter_length:
							ilist = []
						#--------------------------------------------------
					try:
						#skriver datan. Översta formen är för Phonetisarus och den undre är för DEEPphonemizer.
						data.write(wordL + "	" + spliter + "\n")
#						data.write("ukn" + " " + wordL + " " + lineSP[pos2] + "\n")
					except:
						print(("ukn" + " " + wordL + " " + lineSP[pos2]))