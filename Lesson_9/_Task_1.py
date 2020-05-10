newFile = open('myfile.txt', 'w+')
newFile.write('Hello file world!\n')
newFile.seek(0)
print(newFile.read())
