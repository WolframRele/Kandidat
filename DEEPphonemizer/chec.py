from dp.phonemizer import Phonemizer
wordL = []
#Här väljer man modellen man vill använda.
phonemizer = Phonemizer.from_checkpoint('checkpoints/best_model.pt')

#Här väljer man datan vill testa på.
file1 = open("guidevie-s.txt", "r", encoding= "utf-8")

#Processar datan för testning
#---------------------------------
for line in file1:
  wordL.append(line[:-1])
wordLB = [wordL[i:i + 100] for i in range(0, len(wordL), 100)]
#----------------------------------

#Här väljer man vart man vill spara testdatan.
file2 = open("DEEPreulvie-s.txt", "a", encoding= "utf-8")
for L in wordLB:

 #Här överlåt datan till modellen.
  result = phonemizer.phonemise_list(L, lang='ukn')

# Här gissar modellen och sedan skrivs datan till den valda punkten.
  for word, pred in result.predictions.items():
#    print(f'{word} {pred.phonemes} {pred.confidence}')
    file2.write(f'{word} {pred.phonemes} {pred.confidence}' + " " + "\n")
