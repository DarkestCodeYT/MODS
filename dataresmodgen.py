import requests
import zipfile
import os
def loop_input(text,values=['_']):
  value = input(text)
  if value == '':
    loop_input(text)
  else:
    return value if '_' in values or value in values
file_path = 'mod.jar'
output = 'mod'
modID = loop_input('modID> ')
os.makedirs('fabric-'+output, exist_ok=True)
os.makedirs('forge-'+output, exist_ok=True)
username = loop_input('username> ')
forge = loop_input('MineCraft Java Forge? Y or N\nAwnser> ',values=['Y','N'])
if not os.path.exists(file_path):
  with open('forge-'+file_path,'wb') as file:
    file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/forge.jar').content)
  with open('fabric-'+file_path,'wb') as file:
    file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/forge.jar').content)
with zipfile.ZipFile('forge-'+file_path, 'r') as file:
  file.extractall('forge-'+output)
os.remove('forge-'+file_path)
