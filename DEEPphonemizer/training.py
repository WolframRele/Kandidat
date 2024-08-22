from dp.preprocess import preprocess
from dp.train import train
train_data = []
# Denna section formaterar datan för träning
#------------------------------------------
D = open("data2.txt", "r", encoding = "utf-8")
for line in D:
    lineS = line.split(" ")
    train_data.append((lineS[0],lineS[1],lineS[2][:-2]))
print(train_data)
# Pause, så att man kan kolla att datan är korrekt
input()
#-------------------------------------------

#Tränar modellen
#-------------------------------------------
preprocess(config_file='config.yaml', train_data=train_data)
train(config_file='config.yaml', rank=0, num_gpus=1)
#-------------------------------------------