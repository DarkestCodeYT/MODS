import requests
import zipfile
import os
def loop_input(text,values=['_']):
  value = input(text)
  if value == '':
    loop_input(text)
  else:
    if '_' in values or value in values:
      return value 
file_path = 'mod.jar'
output = 'mod'
os.makedirs(output, exist_ok=True)
modID = loop_input('modID> ')
username = loop_input('username> ')
forge = loop_input('MineCraft Java Forge? Y or N\nAwnser> ',values=['Y','N'])
if not os.path.exists(file_path):
  if forge == 'Y':
    with open(file_path,'wb') as file:
      file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/forge.jar').content)
  elif forge == 'N':
    with open(file_path,'wb') as file:
      file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/fabric.jar').content)
  else:
    raise Exception('ERROR')
with zipfile.ZipFile(file_path, 'r') as file:
  file.extractall(output)
os.remove(file_path)
