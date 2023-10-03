import requests
import zipfile
import time
import os
def loop_input(text,values=['_']):
  value = input(text)
  if value == '':
    return loop_input(text)
  if '_' in values or value in values:
    return value
file_path = 'mod.jar'
output = 'mod'
modID = 'shade'#loop_input('modID> ')
username = 'dark_angel071219'#loop_input('username> ')
forge = 'N'#loop_input('MineCraft Java Forge? Y or N\nAwnser> ',values=['Y','N'])
if not os.path.exists(output):
  if forge == 'Y':
    with open(file_path,'wb') as file:
      file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/forge.jar').content)
  elif forge == 'N':
    with open(file_path,'wb') as file:
      file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/templates/fabric.jar').content)
  else:
    raise Exception('ERROR')
  time.sleep(0.1)
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
print(os.listdir(output))
