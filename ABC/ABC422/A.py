S = input()
newWorld = int(S[0])
newStage = int(S[2])

if newStage == 8:
    newWorld += 1
    newStage = 1
else:
    newStage += 1
print(str(newWorld) + '-' + str(newStage))