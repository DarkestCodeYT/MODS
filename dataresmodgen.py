import requests
import zipfile
import os
def loop_input(text):
  value = input(text)
  if value == '':
    loop_input(text)
  else:
    return value
file_path = 'mod.jar'
output = 'mod'
modID = loop_input('modID> ')
username = loop_input('username> ')
if not os.path.exists(file_path):
  with open(file_path,'wb') as file:
    file.write(requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/mods/datapack-resourepack.jar').content)
os.makedirs(output, exist_ok=True)
with zipfile.ZipFile(file_path, 'r') as file:
  file.extractall(output)
os.remove(file_path)
with open(os.path.join(os.path.join(output,'META-INF'),'mods.toml'),'r') as file:
  lines = file.readlines()
lines[7] = f'displayName="{modID}"\n'
lines[10] = f'authors="{username}, ShadeCodesYT, MCreator"'
with open(os.path.join(os.path.join(output,'META-INF'),'mods.toml'),'w') as file:
  file.writelines(lines)
  del lines
#
