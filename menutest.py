Masiv = []

with open ("top5.txt", "r") as textFile:
    for line in textFile:
        info = [ item.strip() for item in line.split(',')]
        Masiv.append(info)

#transform score into str
#get plater name
score = 90
score = str(score)
name = 'DOG'
newScore = [score, name]
Masiv.append(newScore)
Masiv.sort(reverse=True)
top5 = str(Masiv[:5])

f = open('top5.txt', 'w')
i = 0
while(i<5):
    f.write(Masiv[i][0])
    f.write(", ")
    f.write(Masiv[i][1])
    f.write("\n")
    i += 1
print(top5)
f.close()