
Masiv = []

with open ("top5.txt", "r") as textFile:
    for line in textFile:
        info = [ item.strip() for item in line.split(',')]
        Masiv.append(info)

#transform score into str
#get plater name
score = '100'
score = str(score)
name = 'DOG'
secName = 'CAT'
secScore = '70'
newScore = [score, name]
newerScore = [secScore, secName]
Masiv.append(newScore)
Masiv.append(newerScore)
top5 = str(Masiv[:5])

for i in range(len(Masiv)):
    Masiv[i][0] = int(Masiv[i][0])

Masiv.sort(reverse=True)

for i in range(len(Masiv)):
    Masiv[i][0] = str(Masiv[i][0])
print(Masiv)

#Masiv.sort(key=sort_key, reverse=True)