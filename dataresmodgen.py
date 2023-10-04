# https://replit.com/@DarkAngel53/SimilarPointedRuntimelibrary#main.py
import os
def loop_input(text,values=['_']):
  value = input(text)
  if value != '' and '_' in values or value in values:
    return value
  else:
    return loop_input(text,values)
file_path = 'mod.jar'#loop_input('file location> ')
output = file_path.replace(file_path.split('/')[-1],file_path.split('/')[-1].split('.')[0])
if not os.path.exists(output):
  modID = 'shade'#loop_input('modID> ')
  username = 'dark_angel071219'#loop_input('username> ')
  forge = loop_input('MineCraft Java Forge? Y or N\nAwnser> ',values=['Y','N'])
  import requests
  if forge == 'Y':
    with open(file_path,'wb') as file:
      file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/forge.jar').content)
  elif forge == 'N':
    with open(file_path,'wb') as file:
      file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/fabric.jar').content)
  else:
    raise Exception('ERROR')
  import time
  time.sleep(0.1)
  import zipfile
  with zipfile.ZipFile(file_path, 'r') as file:
    file.extractall(output)
  os.remove(file_path)
  os.makedirs(os.path.join(output,'data'), exist_ok=True)
  os.makedirs(os.path.join(output,'assets'), exist_ok=True)
  if forge == 'Y':
    with open(os.path.join(output,'META-INF','mods.toml'),'r') as file:
      lines = file.readlines()
    lines[5] = f'modId="{modID}"'
    lines[7] = f'displayName="{modID}"'
    with open(os.path.join(output,'META-INF','mods.toml'),'w') as file:
      file.writelines(lines)
    del lines
print(f'{os.listdir(output)}')
for dir,folder,file in os.walk(output):
  print(f'\ndirectory: {dir}\nfiles: {file}')
