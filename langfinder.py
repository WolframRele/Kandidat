#Denna fill räkna hur många språk som finns i ett dataset samt hur många ord varje språk har.
from collections import Counter
file = open("TSdata.txt", "r", encoding = "utf-8")
langL = []
for line in file:
    lang,word,fon = line.split(" ")
    langL.append(lang)
langC = Counter(langL)
print(langC)
print(len(langC.keys()))
print(langC.keys())