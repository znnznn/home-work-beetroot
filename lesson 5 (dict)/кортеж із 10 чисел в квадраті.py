myDict = [item for item in range(1, 11)]
sqrt_myDict = {}
for item in myDict:
    sqrt_myDict[item] = item ** 2
print(list(sqrt_myDict.items()))
print(sqrt_myDict)
