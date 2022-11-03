import os
IgnoreList = ['README.txt', 'cfg.py', 'create.py']
AllFiles =  os.listdir()
print('Какие значения подлежат замене для всех файлов:')
replace = input()
print('на какое значение менять:')
rwith = input()

for x in AllFiles:
    if (not x in IgnoreList):
        file = open(x, 'r')
        text = file.read()
        new_text = text.replace(replace, rwith)
        file = open(x, 'w')
        file.write(new_text)
file.close()
