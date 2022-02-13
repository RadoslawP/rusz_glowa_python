import os
os.chdir('/home/raum/Dokumenty/nauka/rusz_glowa_python')

with open('buzzers.csv') as raw_data:
    print(raw_data.read())
